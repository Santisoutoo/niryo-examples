from pyniryo import *

local_mode = False # Or True
workspace_name = "workspace_1" # Robot's Workspace Name

# Set robot address
robot_ip_address_rpi = "x.x.x.x"
robot_ip_address_local = "127.0.0.1"
robot_ip_address = robot_ip_address_local if local_mode else robot_ip_address_rpi

# The pose from where the image processing happens
observation_pose = PoseObject(
x=0.18, y=0.0, z=0.35,
roll=0.0, pitch=1.57, yaw=-0.2,
)

# Center of the conditioning area
place_pose = PoseObject(
x=0.0, y=-0.23, z=0.12,
roll=0.0, pitch=1.57, yaw=-1.57
)

def process(robot):
	robot.move_pose(observation_pose)
	catch_count = 0
	while catch_count < 3:
		ret = robot.get_target_pose_from_cam(workspace_name,
											 height_offset=0.0,
											 shape=ObjectShape.ANY,
											 color=ObjectColor.ANY)
		obj_found, obj_pose, shape, color = ret
		
		if not obj_found:
			continue
		catch_count += 1
		# --- --------- --- #
		# --- YOUR CODE --- #
		# --- --------- --- #
		robot.place_from_pose(place_pose)

if __name__ == '__main__':
	# Connect to robot
	robot = NiryoRobot(robot_ip_address)
	# Calibrate robot if robot needs calibration
	robot.calibrate_auto()
	# Equip tool
	robot.update_tool()
	# Launching main process
	process(robot)
	# Ending
	robot.go_to_sleep()
	# Releasing connection
	robot.close_connection()