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
img_threshold_red = threshold_hsv(img, *ColorHSV.RED.value)
#img_threshold_blue = threshold_hsv(img, *ColorHSV.BLUE.value)


img_close = morphological_transformations(
    img_threshold_red,
    morpho_type=MorphoType.CLOSE,
    kernel_shape=(11,11), kernel_type=KernelType.ELLIPSE
)

img_erode = morphological_transformations(
    img_threshold_red,
    morpho_type=MorphoType.ERODE,
    kernel_shape=(9,9), kernel_type=KernelType.RECT
)

# Show images
show_img("img_threshold_red", img_threshold_red)
show_img("img_close", img_close)
show_img_and_wait_close("img_erode", img_erode)


# it is possible but the picture is bigger than screen
# concat_img = concat_imgs((
#     img_threshold_red, img_threshold_green,
#     img_threshold_blue, img_threshold_any
# ))
# show_img_and_wait_close("RGB-Any", concat_img)