import numpy as np
import cv2
from datetime import *
import time

cap = cv2.VideoCapture('768x576.avi')
current_time=datetime.now()
fgbg = cv2.createBackgroundSubtractorMOG2()

time.sleep(5)

name ='frame_1.jpg'
_,initial_frame = cap.read()
fgmask_1 = fgbg.apply(initial_frame)

cv2.imwrite(name, initial_frame)

img_1 = cv2.imread(name)






name_2='frame_2.jpg'

while(True):
    # Capture frame-by-frame

    _,frame = cap.read()

    if frame is None:
        break

    fgmask = fgbg.apply(frame)



    cv2.imwrite(name_2, frame)
    img_2=cv2.imread(name_2)

    difference = cv2.subtract(img_1,img_2)
    result = not  np.any(difference)
    if result is False:
        print (difference)


    for c in difference:
    	# compute the bounding box of the contour and then draw the
    	# bounding box on both input images to represent where the two
    	# images differ
    	(x, y, w, h) = cv2.boundingRect(c)
    	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


    print (x,y ,w,h)



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
