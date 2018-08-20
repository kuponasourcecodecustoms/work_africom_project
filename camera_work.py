import numpy as np
import cv2
from datetime import *

print ('WELCOME TO THE ____ MONITORING SYSTEM')

cap = cv2.VideoCapture(1)
current_time=datetime.now()

name='Video_Trial_' + current_time.strftime("%Y-%m-%d-%H-%M") + '.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))


while True:
    ret, frame = cap.read()

    out.write(frame)

    cv2.imshow('Video Capture Trial',frame)

    if cv2.waitKey(0) :
            break

cap.release()
out.release()
cv2.destroyAllWindows()
