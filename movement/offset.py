from pyniryo import *

# Offsets allow adjusting a coordinate's position by adding/subtracting values to specific parameters (x, y, z, etc.).
# This avoids rewriting the entire coordinate and makes it easy to reuse a base position with small changes.

# CONSTANTS
IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)

# Define the base pose (starting position)
pick_pose = PoseObject(
    x=0.30, y=0.0, z=0.15,
    roll=0, pitch=1.57, yaw=0.0
)

max_catch_count = 4
catch_count = 0
offset_size = 0.05  # The amount to adjust the position in each step

while catch_count < max_catch_count:
    # Create a new pose by applying an offset to the base pose
    # Here, only the x-coordinate is adjusted, increasing by (catch_count * offset_size) each iteration
    next_place_pose = pick_pose.copy_with_offsets(
        x_offset=catch_count * offset_size,
        # y_offset=catch_count * offset_size,
        # z_offset=catch_count * offset_size
    )
    # Move the robot to the new pose
    robot.place_from_pose(next_place_pose)
    
    catch_count += 1

robot.go_to_sleep()