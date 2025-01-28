from pyniryo import *

IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)

for i in range(2):
    print("CICLO: ", i+1)
    robot.calibrate_auto()
    # check tools avaliable
    robot.update_tool()
    # open gripper || push air from vacum
    robot.release_with_tool()
    robot.move_pose(0.2, -0.1, 0.25, 0.0, 1.57, 0.0)
    # cloase gripper || pull air from vacum
    robot.grasp_with_tool()
    robot.move_pose(0.2, 0.1, 0.25, 0.0, 1.57, 0.0)
    robot.release_with_tool()

robot.close_connection()