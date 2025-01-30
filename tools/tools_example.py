from pyniryo import *

# CONNECTION
IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)

robot.calibrate_auto()


robot.update_tool()
tool_used = ToolID.GRIPPER_1

# To grasp with any tool use 'grasp_with_tool()'
if tool_used in [ToolID.GRIPPER_1, ToolID.GRIPPER_2, ToolID.GRIPPER_3]:
    robot.close_gripper(speed=100)
    robot.open_gripper(speed=100)
elif tool_used == ToolID.ELECTROMAGNET_1:
    pin_electromagnet = PinID.XXX
    robot.setup_electromagnet(pin_electromagnet)
    robot.activate_electromagnet(pin_electromagnet)
elif tool_used == ToolID.VACUUM_PUMP_1:
    robot.push_air_vacuum_pump()
    robot.pull_air_vacuum_pump()

