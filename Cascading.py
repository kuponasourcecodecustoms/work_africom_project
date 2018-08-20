import numpy as np
import cv2

class Cascade(object):

    def __init__(self,info):

        self.info=info

    def define_cascade(self):
        self = cv2.CascadeClassifier(self.info)
