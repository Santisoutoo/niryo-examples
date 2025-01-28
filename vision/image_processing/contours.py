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
#img_threshold_blue = threshold_hsv(img, *ColorHSV.BLUE.value)

img_threshold_any = morphological_transformations(
    img_threshold_any, 
    morpho_type=MorphoType.ERODE,
    kernel_shape=(9,9), 
    kernel_type=KernelType.RECT
)
cnts = biggest_contours_finder(img_threshold_any, 3)
img_contours = draw_contours(img_threshold_any, cnts)
show_img("init", img_threshold_any)
show_img_and_wait_close("img with contours", img_contours)
