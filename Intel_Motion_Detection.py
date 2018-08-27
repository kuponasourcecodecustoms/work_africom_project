import cv2
import numpy as np

import config_setting

cap =  cv2.VideoCapture(0)





sdThresh=10
font = cv2.FONT_HERSHEY_SIMPLEX

def distMap(frame1,frame2):
    frame1_32=np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)

    return dist



_,frame1 = cap.read()
_, frame2 = cap.read()
num =0

while True:

    _, frame3 = cap.read()
    cv2.imshow('framekkk',frame3)

    rows,cols,_ = np.shape(frame3)

    dist = distMap(frame1,frame3)

    frame1 = frame2
    frame2 = frame3

    mod = cv2.GaussianBlur(dist, (9,9),0)

    _, thresh = cv2.threshold(mod , 100, 255 , 0)

    """for (x,y,w,h) in thresh:
            cv2.rectangle(frame3,(x,y),(x+w,y+h),(255,0,0),2)
    """



    _, stDev = cv2.meanStdDev(mod)

    cv2.imshow('dist', mod)
    cv2.putText(frame2, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)

    if stDev > sdThresh:

        num=num+1
        print(str(num) + "Motion detected.. Do something!!!")



    #print (thresh)


    cv2.imshow('frame',frame2)




cap.release()
out.release()
cv2.destroyAllWindows()
