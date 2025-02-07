from pyniryo import *
import cv2 as cv
from matplotlib import pyplot as plt
from utilities import RIGHT_VISION_AREA

# CONNECTION
IP_ADDRESS = "172.16.126.2"
robot = NiryoRobot(IP_ADDRESS)
robot.calibrate_auto()

# Move to vision area
robot.move_pose(RIGHT_VISION_AREA)

# Get image
img_compressed = robot.get_img_compressed()
img = uncompress_image(img_compressed)

# Edge detection with Canny
edges = cv.Canny(img,100,200)

# plot
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 
plt.show()
robot.go_to_sleep()