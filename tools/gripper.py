# To grasp with any tool use 'grasp_with_tool()'
from pyniryo import *
IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)

robot.update_tool()
tool_used = ToolID.GRIPPER_1


if tool_used in [ToolID.GRIPPER_1, ToolID.GRIPPER_2, ToolID.GRIPPER_3]:
    robot.close_gripper(speed=100)
    robot.open_gripper(speed=100)

