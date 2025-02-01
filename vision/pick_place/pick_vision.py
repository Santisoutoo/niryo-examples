from pyniryo import *
from utilities import IP_ADDRESS

# CONNECTION
robot = NiryoRobot(IP_ADDRESS)

# Calibrating the robot automatically to ensure accurate movements
robot.calibrate_auto()

# Initializing variables
offset_size = 0.05  # The distance to offset the placement position for each object
max_catch_count = 3  # Maximum number of objects to catch and place

# Defining the initial position for vision-based picking
posicion_vision = PoseObject(
    -0.0132, 0.1432, 0.2291,
    1.622, 1.433, -2.273
)

# Loop until the desired number of objects have been caught and placed
catch_count = 0
while catch_count < max_catch_count:
    # Move the robot to the observation pose
    robot.move_pose(posicion_vision)

    # Attempt to detect and pick an object using the robot's vision system
    obj_found, shape, color = robot.vision_pick(
        'right_vision', 
        shape=ObjectShape.CIRCLE,  # Looking for objects with a circular shape
        color=ObjectColor.RED      # Looking for objects with a red color
    )

    # If no object is found, wait briefly and calculate a new place pose
    if not obj_found:
        robot.wait(0.1)

        # Calculate the next place pose by applying an offset to the z-coordinate
        next_place_pose = posicion_vision.copy_with_offsets(
            z_offset=catch_count * offset_size
        )

        # Move the robot to the new place pose and place the object
        robot.place_from_pose(next_place_pose)

        # Increment the catch count and continue to the next iteration
        catch_count += 1
        continue

    # If an object is found, move it to a predefined position
    print("Moving object to target location")
    robot.move_pose(0.2242, 0.2232, 0.1367, 2.854, 1.511, -2.626)  # Move to a safe position
    robot.move_pose(0.2242, 0.2232, 0.0511, 2.854, 1.511, -2.626)  # Lower to the placement position
    robot.push_air_vacuum_pump()  # Release the object

    # Increment the catch count
    catch_count += 1

# Put the robot to sleep after completing the task
robot.go_to_sleep()