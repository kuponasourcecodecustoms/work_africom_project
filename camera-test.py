import numpy as np
import cv2
from datetime import *


cap = cv2.VideoCapture('x7y.mp4')
current_time=datetime.now()

#ame='Video_Trial_' + current_time.strftime("%Y-%m-%d-%H-%M") + '.mp4'
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))
#fgbg =  cv2.createBackgroundSubtractorMOG2()
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
face_cascade_3= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade_2= cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
lowerbody_cascade= cv2.CascadeClassifier('haarcascade_lowerbody.xml')
profile_face_cascade= cv2.CascadeClassifier('haarcascade_profileface.xml')
upperbody_cascade= cv2.CascadeClassifier('haarcascade_upperbody.xml')


while(True):
    # Capture frame-by-frame

    _,frame = cap.read()

    #edges=cv2.Canny(frame,100,200)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray,9,5)

    facec = face_cascade.detectMultiScale(gray,9,5)
    facec3 = face_cascade_3.detectMultiScale(gray,9,5)
    facec2 = face_cascade_2.detectMultiScale(gray,9,5)
    lbc= lowerbody_cascade.detectMultiScale(gray,9,5)
    pfc = profile_face_cascade.detectMultiScale(gray,9,5)
    upc = upperbody_cascade.detectMultiScale(gray,9,5)


    for (x,y,w,h) in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


    for (x,y,w,h) in facec:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in facec3:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in facec2:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in lbc:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in pfc:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in upc:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


    #cv2.imshow('im',edges)

    #out.write(frame)
    cv2.line(frame,(0,0),(150,150),(255,0,0))


    # Display the resulting frame
    cv2.imshow('Window Monitoring Frame',frame)
    #cv2.imshow('Movement',fgmask)
    key = cv2.waitKey(33)
    if  key== 27:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
