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
# It is a python object that stores roll, pitch and yaw
# That it can be also converted into list via to_list()

pose_object_test = PoseObject(
    0.1402,
    -0.0001,
    0.2033,
    0.003,
    0.751,
    -0.001
)

# print(pose_object_test)
# if we only want the values of the axis,
# we may use the function bellow

# print(pose_object_test.to_list())

# output: [0.1402, -0.0001, 0.2033, 0.003, 0.751, -0.001]
# If we compare this to __str__ , setters and fuction methods
# output: x = 0.1402, y = -0.0001, z = 0.2033
#         roll = 0.003, pitch = 0.751, yaw = -0.001
# it is clearly much easier to operate with this data structre