from pyniryo import *

# Connect to robot & calibrate
IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)
robot.calibrate_auto()

# SET CAMARA POSITION
robot.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
# --- --------- --- #
# --- YOUR CODE --- #
# --- --------- --- #
# Releasing connection

robot.close_connection()