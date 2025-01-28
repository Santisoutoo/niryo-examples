from pyniryo import *

# CONSTANS
IP_ADDRESS = "10.10.10.10"
POSITION = [-0.15, 0.3, 0.2, 0.3, -0.6, 0.0]
POSITION_2 = [-0.5, -0.6, 0.0, 0.3, 0.0, 0.0]

# CONNECTION
robot = NiryoRobot(IP_ADDRESS)


# It is posible to provide 6 float numbers to
# .move_joins()
# or a list o 6 floats

print("MOVING JOINS WITH SETTERS AND FLOATS")
# Moving Joints with setter & a list of floats
robot.joints = 0.2, -0.4, 0.0, 0.0, 0.0, 0.0
print("MOVING JOINS WITH SETTERS AND LIST")
robot.joints = POSITION

# # Moving Joints with function & 6 floats
print("MOVING JOINS WITH FUNCTION AND FLOATS")
# Moving Joints with function & a list of floats
robot.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
print("MOVING JOINS WITH SETTERS AND LIST")
# Moving Joints with setter & 6 floats
robot.move_joints(POSITION_2)


robot.close_connection()
