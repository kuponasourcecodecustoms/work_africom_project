import numpy as np
import cv2
from datetime import *
import time

cap = cv2.VideoCapture('768x576.avi')
current_time=datetime.now()
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

time.sleep(5)







name_2='frame_2.jpg'

while(True):
    # Capture frame-by-frame

    _,frame = cap.read()

    if frame is None:
        break


    fgmask = fgbg.apply(frame3)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)







    _,analysis = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)








    cv2.imshow('analysis',analysis)


    _,contours, _ = cv2.findContours(analysis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in  contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        cv2.rectangle(display, (x,y), (x+w,y+h), (255, 0, 0), 2)






    cv2.imshow('frame',fgmask)
    # Display the resulting frame
    cv2.imshow('Window Monitoring Frame',frame)
    #cv2.imshow('Movement',fgmask)
    key = cv2.waitKey(1)
    if  key== 27:
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
