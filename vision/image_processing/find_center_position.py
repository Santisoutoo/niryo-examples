from pyniryo import *

# CONSTANS
IP_ADDRESS = "10.10.10.10"
GREEN_MIN_HSV = [40, 120, 75]
GREEN_MAX_HSV = [90, 255, 255]
ANY_MIN_HSV = [0, 50, 100]
ANY_MAX_HSV = [179, 255, 255]

# CONNECTION
robot = NiryoRobot(IP_ADDRESS)
robot.calibrate_auto()# Getting calibration param


# LEFT VISION AREA
observation_pose = PoseObject(
    0.0126, -0.1571, 0.2967,
    -2.979, 1.456, 0.832
)

robot.move_pose(observation_pose)

# TAKE PHOTO
img_compressed = robot.get_img_compressed()
# Uncompressing image
img = uncompress_image(img_compressed)
# Displaying
#show_img_and_wait_close("img_stream", img)

# FILTER
# You can use the class already defined
img_threshold_any = threshold_hsv(img, *ColorHSV.ANY.value)

img_threshold_any = morphological_transformations(
    img_threshold_any, 
    morpho_type=MorphoType.ERODE,
    kernel_shape=(9,9), 
    kernel_type=KernelType.RECT
)
cnt = biggest_contour_finder(img_threshold_any)
cnt_barycenter = get_contour_barycenter(cnt)
cx, cy = cnt_barycenter
cnt_angle = get_contour_angle(cnt)
img_debug = draw_contours(img_threshold_any, [cnt])
img_debug = draw_barycenter(img_debug, cx, cy)
img_debug = draw_angle(img_debug, cx, cy, cnt_angle)
show_img_and_wait_close("Image with contours, barycenter and angle", img_debug)
