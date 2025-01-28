from pyniryo import *

observation_pose = PoseObject(
    x=0.18, y=0.0, z=0.35,
    roll=0.0, pitch=1.57, yaw=-0.2,
)

# Connecting to robot
robot = NiryoRobot("10.10.10.10")
robot.calibrate_auto()# Getting calibration param
mtx, dist = robot.get_camera_intrinsics()

# Moving to observation pose
robot.move_pose(observation_pose)

while "User do not press Escape neither Q":
    # Getting image
    img_compressed = robot.get_img_compressed()
    # Uncompressing image
    img_raw = uncompress_image(img_compressed)
    # Undistorting
    img_undistort = undistort_image(img_raw, mtx, dist)# - Display
    # Concatenating raw image and undistorted image
    concat_ims = concat_imgs((img_raw, img_undistort))# Showing images
    key = show_img("Images raw & undistorted", img_undistort, wait_ms=30)
    if key in [27, ord("q")]:
        # Will break loop if the user press Escape or Q
        break