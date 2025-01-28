# Offsets are used to change the position of a coordenate
# by adjusting a parameter and not writting the same point 
# changing only one parameter

from pyniryo import *


# CONSTANS
IP_ADDRESS = "10.10.10.10"


# CONNECTION
robot = NiryoRobot(IP_ADDRESS)


pick_pose = PoseObject(
    x=0.30, y=0.0, z=0.15,
    roll=0, pitch=1.57, yaw=0.0
)
first_place_pose = PoseObject(
    x=0.0, y=0.2, z=0.15,
    roll=0, pitch=1.57, yaw=0.0
)

for i in range(8):
    print("i = ", i)
    robot.move_pose(pick_pose)
    print("OFFSET")
    new_place_pose = first_place_pose.copy_with_offsets(x_offset=0.05 * i)
    robot.move_pose(new_place_pose)