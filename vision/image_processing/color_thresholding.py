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
img_threshold_blue = threshold_hsv(img, *ColorHSV.BLUE.value)


# Or set your owns values
img_threshold_green = threshold_hsv(
    img, 
    list_min_hsv=GREEN_MIN_HSV, list_max_hsv=GREEN_MAX_HSV, 
    reverse_hue=False
)
img_threshold_any = threshold_hsv(
    img, 
    list_min_hsv=ANY_MIN_HSV, list_max_hsv=ANY_MAX_HSV, 
    reverse_hue=False
)

# Show images
show_img("img_threshold_red", img_threshold_red)
show_img("img_threshold_green", img_threshold_green)
show_img("img_threshold_blue", img_threshold_blue)
show_img_and_wait_close("img_threshold_any", img_threshold_any)


# it is possible but the picture is bigger than screen
# concat_img = concat_imgs((
#     img_threshold_red, img_threshold_green,
#     img_threshold_blue, img_threshold_any
# ))
# show_img_and_wait_close("RGB-Any", concat_img)