from pyniryo import *
import cv2 as cv
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

# initialize variables
low_H, low_S, low_V = 0, 40, 80
high_H, high_S, high_V = 180, 255, 255

# Create window for color thresholding
cv.namedWindow("Object Detection")

class TrackBarUpdate():
    """
    This class handles the updating of trackbars for HSV color filtering.
    It stores the current values of the trackbars for the low and high ranges of the H, S, and V channels.
    """

    def __init__(self, low_h = 0, high_h = 40, low_s = 80, high_s =180, low_v=255, high_v=255):
        self.low_h = low_h
        self.high_h = high_h
        self.low_s = low_s
        self.high_s = high_s
        self.low_v = low_v
        self.high_v = high_v
        
    def update_low_H(self, val):
        self.low_h = val
        cv.setTrackbarPos("Low H", "Object Detection", self.low_h)

    def update_high_H(self, val):
        self.high_h = val
        cv.setTrackbarPos("High H", "Object Detection", self.high_h)

    def update_low_S(self, val):
        self.low_s = val
        cv.setTrackbarPos("Low S", "Object Detection", self.low_s)

    def update_high_S(self, val):
        self.high_s = val
        cv.setTrackbarPos("High S", "Object Detection", self.high_s)

    def update_low_V(self, val):
        self.low_v = val
        cv.setTrackbarPos("Low V", "Object Detection", self.low_v)

    def update_high_V(self, val):
        self.high_v = val
        cv.setTrackbarPos("High V", "Object Detection", self.high_v)

trackbar = TrackBarUpdate(low_H, high_H, low_S, high_S, low_V, high_V)

# Trackbars Creation 
cv.createTrackbar("Low H", "Object Detection", low_H, 180, trackbar.update_low_H)
cv.createTrackbar("High H", "Object Detection", high_H, 180, trackbar.update_high_H)
cv.createTrackbar("Low S", "Object Detection", low_S, 255, trackbar.update_low_S)
cv.createTrackbar("High S", "Object Detection", high_S, 255, trackbar.update_high_S)
cv.createTrackbar("Low V", "Object Detection", low_V, 255, trackbar.update_low_V)
cv.createTrackbar("High V", "Object Detection", high_V, 255, trackbar.update_high_V)

while True:

    # Change from BGR (default model in openCV) to HSV
    frame_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    frame_threshold = cv.inRange(
        frame_HSV, 
        (trackbar.low_h, trackbar.low_s, trackbar.low_v), 
        (trackbar.high_h, trackbar.high_s, trackbar.high_v)
    )
    
    cv.imshow("Original Image", img)
    cv.imshow("Object Detection", frame_threshold)
    
    # Salir con 'q' o ESC
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break

cv.destroyAllWindows()
robot.go_to_sleep()
