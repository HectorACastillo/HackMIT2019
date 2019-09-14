# recog.py
# Vision - Anthony Nardomarino
# Python v2.7
# dependencies:
#   conda install future
# pip install ibm_watson
# 9 14 2019

from __future__ import print_function
from ibm_watson import VisualRecognitionV3
import json

def recog():

    """
    Reads local image frame.png and classifies it
    Returns a string representing a dictionary of potential
        classifications and their associated probabilities
    """


    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        iam_apikey='aFDsruSB-F1KcO-N4VXa6OhlH7xdhJwKYaodeLKVQeXB'
    )
    # visual_recognition.disable_SSL_verification()

    with open('./frame.jpg', 'rb') as image_file:
        classes = visual_recognition.classify(
            image_file,
            threshold='0.6',
            owners=["me","IBM"]).get_result()
        return (json.dumps(classes, indent=2))
