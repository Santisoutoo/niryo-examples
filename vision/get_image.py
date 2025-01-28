from pyniryo import *

# CONSTANS
IP_ADDRESS = "10.10.10.10"
# CONNECTION
robot = NiryoRobot(IP_ADDRESS)

# Getting image
img_compressed = robot.get_img_compressed()
# Uncompressing image
img = uncompress_image(img_compressed)# Displaying
show_img_and_wait_close("img_stream", img)