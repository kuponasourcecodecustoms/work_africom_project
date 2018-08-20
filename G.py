import numpy as np
import cv2
from datetime import *
import time

cap = cv2.VideoCapture('768x576.avi')
current_time=datetime.now()
fgbg = cv2.createBackgroundSubtractorMOG2()

time.sleep(5)







name_2='frame_2.jpg'

while(True):
    # Capture frame-by-frame

    _,frame = cap.read()

    if frame is None:
        break

    fgmask = fgbg.apply(frame)




    ret,thresh = cv2.threshold(fgmask,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)




    cv2.imshow('frame',fgmask)
    # Display the resulting frame
    cv2.imshow('Window Monitoring Frame',frame)
    #cv2.imshow('Movement',fgmask)
    key = cv2.waitKey(1)
    if  key== 27:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
