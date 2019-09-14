# -----------------------------------------------------------
# Video Catpure
# Author: Tony Terrasa
# Dependencies:
# -- python version: 2.7
# --
# image input
# source: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
# image tracking
# source: https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/
#
# Notes:
#       - logitech reads in (480x640) images
#       - Tony's webcam reads in (480x640) images
# -----------------------------------------------------------

from __future__ import print_function
import numpy as np
import cv2
import time

"""
OPENCV_OBJECT_TRACKERS = {
	"csrt": cv2.TrackerCSRT_create,
	"kcf": cv2.TrackerKCF_create,
	"boosting": cv2.TrackerBoosting_create,
	"mil": cv2.TrackerMIL_create,
	"tld": cv2.TrackerTLD_create,
	"medianflow": cv2.TrackerMedianFlow_create,
	"mosse": cv2.TrackerMOSSE_create
}
"""



# on TonyT computer:
# comp camera: index 0
# logitech: index 2
cap = cv2.VideoCapture(2) # input the indeex of the video you want
#tracker = cv2.TrackerMIL_create()
tracking = False

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #print(frame.shape)

    # if tracking:
    #     (success, box) = tracker.update(frame)
    #
	# 	# check to see if the tracking was a success
    #     if success:
    #         (x, y, w, h) = [int(v) for v in box]
    #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)

    # if the 's' key is selected, we are going to "select" a bounding
	# box to track
    if key == ord("s"):
    	# select the bounding box of the object we want to track (make
		# sure you press ENTER or SPACE after selecting the ROI)
        initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        print(type(initBB))
        tracker.init(frame, initBB)
        tracking = True

    time.sleep()

    if key == ord('w'):
        cv2.imwrite('bottle.png', frame)

    # stop outputting if the user types 'q'
    if key & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
