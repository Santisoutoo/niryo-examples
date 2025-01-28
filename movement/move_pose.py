from pyniryo import *

# CONSTANS
IP_ADDRESS = "10.10.10.10"


# CONNECTION
robot = NiryoRobot(IP_ADDRESS)


# It is possible to move the different axis in 3 different ways
# 6 Floats: x, y, z, roll, pitch, yaw
# list of 6 floats [x, y, z, roll, pitch, yaw]
# A PoseObject which stores the values "x, y, z, roll, pitch, yaw"


pose_target = [0.2, 0.0, 0.3, 0.0, 0.0, 0.0]
pose_target_obj = PoseObject(0.2, 0.0, 0.2, 0.0, 0.0, 0.0)

print("MOVING WITH POSE FUNCTION AND FLOATS")
robot.move_pose(0.2, 0.0, 0.2, 0.0, 0.0, 0.0)
print("MOVING WITH POSE FUNCTION AND LIST")
robot.move_pose(pose_target)
print("MOVING WITH POSE FUNCTION AND POSE OBJET")
robot.move_pose(pose_target_obj)

# Moving Pose with setter
print("MOVING WITH POSE SETTER AND FLOATS")
robot.pose = (0.2, 0.0, 0.2, 0.0, 0.0, 0.0)
print("MOVING WITH POSE SETTER AND LIST")
robot.pose = pose_target
print("MOVING WITH POSE SETTER AND POSE OBJET")
robot.pose = pose_target_obj