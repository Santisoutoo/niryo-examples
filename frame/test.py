from pyniryo import *

IP_ADDRESS = "10.10.10.10"
GRIPPER_SPEED = 400

if __name__ == '__main__':

    robot = NiryoRobot(IP_ADDRESS)
    point_o = [0.15, 0.15, 0]
    point_x = [0.25, 0.2, 0]
    point_y = [0.2, 0.25, 0]

    robot.save_dynamic_frame_from_points(
        "test", 
        "description", 
        point_o, 
        point_x, 
        point_y
    )

    print(robot.get_saved_dynamic_frame_list())
    # Check creation of the frame
    info = robot.get_saved_dynamic_frame("test")
    print(info)# Pick
    robot.open_gripper(GRIPPER_SPEED)
    # Move to the frame
    initial_pose = PoseObject(0, 0, 0, 0, 1.57, 0)
    robot.move_pose(initial_pose, "test")
    robot.close_gripper(GRIPPER_SPEED)# Move in frame
    robot.move_linear_relative([0, 0, 0.1, 0, 0, 0], "test")
    robot.move_relative([0.1, 0, 0, 0, 0, 0], "test")
    robot.move_linear_relative([0, 0, -0.1, 0, 0, 0], "test")# Place
    robot.open_gripper(GRIPPER_SPEED)
    robot.move_linear_relative([0, 0, 0.1, 0, 0, 0], "test")# Home
    robot.move_joints(0, 0.5, -1.25, 0, 0, 0)# Delete frame
    robot.delete_dynamic_frame("test")