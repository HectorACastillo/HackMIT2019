import cv2
import numpy as np


def draw_tracking_box(box, image):
    """
    draws a bounding box

    box: tuple of the bounding box in format x,y,x,h where x,y are the coordinates
         and w,h and the width and height of the box respectively
    """
    (x, y, w, h) = [int(v) for v in box]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


def draw_translation(output_string, location, image):
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(image, output_string, location, font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    return image


    # image will be a numpy array
    # location will be a tple
    # output ewill be string
    # https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
    # opencv draw reactangle
    # opencv write text
    # return the image
