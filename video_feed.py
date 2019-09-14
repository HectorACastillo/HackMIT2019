# -----------------------------------------------------------
# Video Catpure
# Author: Tony Terrasa
# Dependencies:
# -- python version: 2.7
# -- opencv-contrib 3.4.4.19 #IMPORTANT THAT YOU INSTALL THE CONTRIB VERSION OF OPENCV
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

from recog import recog
from video_tools import draw_tracking_box, draw_translation, translate
from parse_label import parse_label
from change_lang import change_lang

"""
types of trackers
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


def make_tracker(): return cv2.TrackerKCF_create()


# on TonyT computer:
# comp camera: index 0
# logitech: index 2
cap = cv2.VideoCapture(2) # input the indeex of the video you want
tracker = make_tracker() # for tracking the object in the frame

# location of the object 
# this cariable not being None signifies that you are tracking an object
current_box = None 

# lsat translation of object
# this variable not being None indicates that a translation has been made
translated = None 

key = True  # user input must be True to enter while loop

output_name = "output"

# press 'q' to quit the operation
while(key and key & 0xFF != ord('q')):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #print(frame.shape)

    # if already tracking, update the location of the object
    if current_box:
        # find the location of the object
        (success, current_box) = tracker.update(frame)

        # if found, draw a box around it
        if success: draw_tracking_box(current_box, frame)

    # receive user input
    key = cv2.waitKey(1)


    # must be tracking an object
    if current_box and key == ord("t"):
        # Upon pressing 't', it will call the function to trasnlate and display the output
        to_translate, translated = translate(current_box, frame, "es")


    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track 
        # (make sure you press ENTER or SPACE after selecting the ROI)
        initBB = cv2.selectROI(output_name, frame, fromCenter=False)
        tracker.init(frame, initBB)

        # keep track of the region of interest
        current_box = initBB

    if key == ord("r"):
        current_box = None
        translated = None
        initBB = None
        tracker = make_tracker() # for tracking the object in the frame



    # if a translation has been made, draw it on the box 
    if translated: 
        location = (int(current_box[0]), int(current_box[1]))
        # print(translated)
        frame = draw_translation(translated, location, frame)

    cv2.imshow(output_name, frame)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
