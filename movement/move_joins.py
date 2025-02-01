from pyniryo import *

# CONSTANTS
IP_ADDRESS = "10.10.10.10"
POSITION = [-0.15, 0.3, 0.2, 0.3, -0.6, 0.0]
POSITION_2 = [-0.5, -0.6, 0.0, 0.3, 0.0, 0.0]

# CONNECTION
robot = NiryoRobot(IP_ADDRESS)

# It is possible to provide either 6 float numbers or a list of 6 floats to .move_joints()

print("MOVING JOINTS WITH SETTERS AND FLOATS")
# Moving Joints using the setter with individual floats
robot.joints = 0.2, -0.4, 0.0, 0.0, 0.0, 0.0
print("MOVING JOINTS WITH SETTERS AND LIST")
# Moving Joints using the setter with a predefined list of floats
robot.joints = POSITION

# Moving Joints using the function with individual floats
print("MOVING JOINTS WITH FUNCTION AND FLOATS")
robot.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
print("MOVING JOINTS WITH FUNCTION AND LIST")
# Moving Joints using the function with a predefined list of floats
robot.move_joints(POSITION_2)


robot.close_connection()