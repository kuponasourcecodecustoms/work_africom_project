import numpy as np
import cv2
from datetime import *

print ('WELCOME TO THE ____ MONITORING SYSTEM')
cap = cv2.VideoCapture(1)

current_time=datetime.now()

name='Video_Trial_' + current_time.strftime("%Y-%m-%d-%H-%M") + '.mp4'



# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))


while(cap.isOpened()):
    ret, frame = cap.read()


    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,29,0.005)


    frame[dst>0.00001*dst.max()]=[0,0,255]

    out.write(frame)

    cv2.imshow('Video Capture Trial',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break








# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
