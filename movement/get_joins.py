from pyniryo import *

# CONSTANS
IP_ADDRESS = "10.10.10.10"
HOME_POSITION = [
    0.0007930673506395536,
    0.49940895727663126,
    -1.2506181983468665,
    -0.0014413271980928677,
    0.004509288773864029,
    0.0031606151655640957
]

# CONNECTION
robot = NiryoRobot(IP_ADDRESS)


# It's possible to read joins' postion in two ways
# With a function or via getter

# Getting Joints with function
joints_read = robot.get_joints()# Getting Joints with getter
joints_read_2 = robot.joints

print(f"Joins position with funtion {joints_read}")
print(f"Joins position with getter {joints_read_2}")

# As we are in python we can assing each joint with a variable

j1,j2,j3,j4,j5,j6 = joints_read

print(
    f"""
    J1 = {j1:.3f}
    J2 = {j2:.3f}
    J3 = {j3:.3f}
    J4 = {j4:.3f}
    J5 = {j5:.3f}
    J6 = {j6:.3f}
    """
)

robot.close_connection()