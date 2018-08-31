from config_setting import *
from flask import Flask, render_template, Response


print ('WELCOME TO THE ____ MONITORING SYSTEM')

cap = cv2.VideoCapture(1)






def video_record(camera):
    name='Motion_Detected_at:' + current_time.strftime("%Y-%m-%d-%H-%M") + '.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))


sdThresh=4.5
font = cv2.FONT_HERSHEY_SIMPLEX
fgbg = cv2.createBackgroundSubtractorMOG2()

kernel1 = np.ones((5,5),np.uint8)



img = np.zeros((300,512,3), np.uint8)*255
img[:]=[0,0,255]
cv2.namedWindow('settingWindow')
cv2.createTrackbar('Standard Deviation Threshold Limit','settingWindow',4,30,nothing)

switch = '0 :OFF\n1 :ON'
cv2.createTrackbar(switch, 'settingWindow',0,1,nothing)






_,frame1 = cap.read()
_, frame2 = cap.read()
num=0

while True:
    _, frame3 = cap.read()


    dist = distMap(frame1,frame3)

    frame1 = frame2
    frame2 = frame3

    mod = cv2.GaussianBlur(dist, (9,9),0)


    _, thresh = cv2.threshold(mod , 127, 255 , 0)


    _, stDev = cv2.meanStdDev(mod)







    sdThresh = cv2.getTrackbarPos('Standard Deviation Threshold Limit','settingWindow')


    fgmask = fgbg.apply(frame3)
    cv2.imshow('fgmask',fgmask)
    erosion = cv2.erode(fgmask,kernel1,iterations = 1)
    cv2.imshow('erosionS',erosion)



    fgmask = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel1)

    cv2.imshow('morphed',fgmask)
    _,analysis = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)
    cv2.imshow('lol',analysis)




    display = frame3




    if stDev > sdThresh:
        _,contours, _ = cv2.findContours(analysis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for contour in  contours:
            (x,y,w,h) = cv2.boundingRect(contour)

            cv2.rectangle(frame3, (x,y), (x+w,y+h), (255, 0, 0), 2)

        num=num+1
        print(str(num) + "Motion detected..User Informed!!!\n")
        if num==1:
            #auto_email()
            pass








    switch1 = cv2.getTrackbarPos(switch,'settingWindow')
    if switch1 ==1:
        cv2.imshow('LIVE STREAM',display)
    if switch1 ==0:
        cv2.destroyWindow('LIVE STREAM')

    cv2.imshow('settingWindow',img)

    key = cv2.waitKey(33)
    if  key== 27 or ord == 'q':
        break

cap.release()
out.release()
cv2.destroyAllWindows()
