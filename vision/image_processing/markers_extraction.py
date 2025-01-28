from pyniryo import *

# CONSTANS
IP_ADDRESS = "10.10.10.10"

# CONNECTION
robot = NiryoRobot(IP_ADDRESS)

# TAKE PHOTO
img_compressed = robot.get_img_compressed()
# Uncompressing image
img = uncompress_image(img_compressed)


img_workspace = extract_img_workspace(img, workspace_ratio=1.0)
show_img("init", img)
show_img_and_wait_close("img_workspace", img_workspace)