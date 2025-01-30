from pyniryo import *

# Offsets are used to change the position of a coordenate
# by adjusting a parameter and not writting the same point
# changing only one parameter

# CONSTANS
IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)

pick_pose = PoseObject(
    x=0.30, y=0.0, z=0.15,
    roll=0, pitch=1.57, yaw=0.0
)

max_catch_count = 4
catch_count = 0
offset_size = 0.05

while catch_count > max_catch_count:

    next_place_pose = pick_pose.copy_with_offsets(
        x_offset=catch_count * offset_size,
        # y_offset=catch_count * offset_size,
        # z_offset=catch_count * offset_size
    )
    robot.place_from_pose(next_place_pose)

robot.go_to_sleep()
