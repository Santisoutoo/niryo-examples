from pyniryo import *

# CONNECTION
IP_ADDRESS = "10.10.10.10"
robot = NiryoRobot(IP_ADDRESS)

# It's possible to read axis postion in two ways
# With a function or via getter

# Function
pose_read = robot.get_pose()
# Getter
pose_read_2 = robot.pose

print(pose_read)
print()
print(pose_read_2)


# Using PoseObject
# It is a python object that stores x, y, z, roll, pitch and yaw parameters
# The units used are RADIANS


pose_object_test = PoseObject(
    0.1402,
    -0.0001,
    0.2033,
    0.003,
    0.751,
    -0.001
)

# Print the pose object to see its values:
# Output: x = 0.1402, y = -0.0001, z = 0.2033
#         roll = 0.003, pitch = 0.751, yaw = -0.001

# You can also convert these values into a list using the to_list() method.
# This makes it easier to display and work with the data.

# Example:
# print(pose_object_test.to_list())
# Output: [0.1402, -0.0001, 0.2033, 0.003, 0.751, -0.001]

# Comparing to_list() with other methods, using to_list() is more convenient
# because you can directly use the list in instructions, like moving a robot,
# without manually entering the data each time.