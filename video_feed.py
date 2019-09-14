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
from video_tools import draw_tracking_box, draw_translation
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



# on TonyT computer:
# comp camera: index 0
# logitech: index 2
cap = cv2.VideoCapture(0) # input the indeex of the video you want
tracker = cv2.TrackerKCF_create() # for tracking the object in the frame
current_box = None # location of the object
translated = None # last translation of object

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #print(frame.shape)

    # if already tracking
    if current_box:
        # find the locaiton of the object
        (success, current_box) = tracker.update(frame)

        # if found, draw a box around it
        if success: draw_tracking_box(current_box, frame)



    # receive use input
    key = cv2.waitKey(1)

    #print(key)
    
    if key == ord("w"):
        """
        Upon pressing w, it will call the function to trasnlate and display the output
        """

        print("translation")
        if not current_box:
            print("stop")

        x,y,w,h = [int(p) for p in current_box] # convert the coordinates to integers
        cv2.imwrite('frame.jpg', frame[y:y+h,x:x+w]) # save image of just the 
        recognition_output = recog('frame.jpg') # run the image recognition
        to_translate = parse_label(recognition_output) # get the name of the object in english
        translated = change_lang(to_translate, "es") # translate the object into specified language
        print(to_translate, translated) # print in the terminal



    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        initBB = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
        tracker.init(frame, initBB)

        # keep track of the region of interest
        current_box = initBB


    if translated: frame = draw_translation(translated, (x,y), frame)
    cv2.imshow('frame', frame)

    # stop outputting if the user types 'q'
    if key & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
