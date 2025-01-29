from pyniryo import *
from utilities import *


# Connecting to robot
robot = NiryoRobot(IP_ADDRESS)
robot.calibrate_auto()# Getting calibration param
#mtx, dist = robot.get_camera_intrinsics()


# Initializing variables
offset_size =   0.05
max_catch_count = 3

posicion_vision = PoseObject(
    -0.0132, 0.1432, 0.2291,
    1.622, 1.433, -2.273
)


# Loop until enough objects have been caught
catch_count = 0
while catch_count < max_catch_count:
    # Moving to observation pose
    robot.move_pose(posicion_vision)
    # Trying to get object via Vision Pick
    obj_found, shape, color = robot.vision_pick('right_vision')


    if not obj_found:
        robot.wait(0.1)
        # Calculate place pose and going to place the object
        next_place_pose = posicion_vision.copy_with_offsets(
            #x_offset=catch_count * offset_size,
            #y_offset=catch_count * offset_size,
            z_offset=catch_count * offset_size

        )
        robot.place_from_pose(next_place_pose)
        catch_count +=1
        continue



    print("moving")
    robot.move_pose(0.2242, 0.2232,0.1367,2.854,1.511,-2.626)
    robot.move_pose(0.2242, 0.2232,0.0511,2.854,1.511,-2.626)
    robot.push_air_vacuum_pump()

    catch_count +=1



robot.close_connection()