# Issue with Using Frames in Niryo  

Hello everyone,

I've been trying to use a frame that I created with Python and another one in the Niryo app. However, when I try to execute instructions such as:

```python
robot.move_linear_relative([0, 0, 0.1, 0, 0, 0], "frame")
```

The robot executes the script but completely ignores the movement instruction. Additionally, when I try to run the equivalent block in the Niryo app (which moves the robot relative to a frame), nothing happens even though the target position is well within the robot's workspace.

On the other hand, the program in the documentation also does not work. It only shows the created frames, but no movement is performed.

## Code Used

```python
print(robot.get_saved_dynamic_frame_list())

# Verify frame creation
info = robot.get_saved_dynamic_frame("test")
print(info)

# Pick an object
robot.open_gripper(GRIPPER_SPEED)

# Move to the frame
initial_pose = PoseObject(0, 0, 0, 0, 1.57, 0)
robot.move_pose(initial_pose, "test")

robot.close_gripper(GRIPPER_SPEED)

# Move within the frame
robot.move_linear_relative([0, 0, 0.1, 0, 0, 0], "test")
robot.move_relative([0.1, 0, 0, 0, 0, 0], "test")
robot.move_linear_relative([0, 0, -0.1, 0, 0, 0], "test")

# Place the object
robot.open_gripper(GRIPPER_SPEED)
robot.move_linear_relative([0, 0, 0.1, 0, 0, 0], "test")

# Return to home position
robot.move_joints(0, 0.5, -1.25, 0, 0, 0)

# Delete the frame
robot.delete_dynamic_frame("test")
```

## Output Obtained

```
Connected to server (10.10.10.10) on port: 40001

[['dynamic_frame'], ['description']]
['dynamic_frame', 'description', [0.15, 0.15, 0.0, 0.0, -0.0, 0.46364760900080637]]

Disconnected from robot
```

## Issue

The frame seems to be created correctly, but the robot does not execute movements relative to the frame, neither in the app nor in the script.

Has anyone experienced this issue before or have any suggestions?

Thanks.