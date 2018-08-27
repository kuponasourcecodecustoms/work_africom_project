from config_setting import *

print ('WELCOME TO THE ____ MONITORING SYSTEM')

cap = cv2.VideoCapture('768x576.avi')




def video_record(camera):
    name='Motion_Detected_at:' + current_time.strftime("%Y-%m-%d-%H-%M") + '.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(name,fourcc, 20.0, (640,480))


sdThresh=4.5
font = cv2.FONT_HERSHEY_SIMPLEX
fgbg = cv2.createBackgroundSubtractorMOG2()



img = np.zeros((300,512,3), np.uint8)*255
img[:]=[0,0,255]
cv2.namedWindow('settingWindow')
cv2.createTrackbar('Standard Deviation Threshold Limit','settingWindow',4,10,nothing)

switch = '0 :OFF\n1 :ON'
cv2.createTrackbar(switch, 'settingWindow',0,1,nothing)





_,frame1 = cap.read()
_, frame2 = cap.read()
num=0

while True:
    _, frame3 = cap.read()

    #rows,cols,_ = np.shape(frame3)
    dist = distMap(frame1,frame3)




    frame1 = frame2
    frame2 = frame3

    mod = cv2.GaussianBlur(dist, (9,9),0)
    cv2.imshow('blurred',mod)







    _, thresh = cv2.threshold(mod , 100, 255 , 0)
    _,analysis = cv2.threshold(dist,100,255,cv2.THRESH_BINARY)
    _,analysis1 = cv2.threshold(dist,100,255,cv2.THRESH_BINARY_INV)
    _,analysis2 = cv2.threshold(dist,100,255,cv2.THRESH_TRUNC)
    _,analysis3 = cv2.threshold(dist,100,255,cv2.THRESH_TOZERO)
    _,analysis4 = cv2.threshold(dist,100,255,cv2.THRESH_TOZERO_INV)

    cv2.imshow('analysis',analysis)
    cv2.imshow('analysis1',analysis1)
    cv2.imshow('analysis2',analysis2)
    cv2.imshow('analysis3',analysis3)
    cv2.imshow('analysis4',analysis4)

    th2 = cv2.adaptiveThreshold(analysis3,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(analysis3,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)

    cv2.imshow('th2',th2)
    cv2.imshow('th3',th3)


    medic = fgbg.apply(analysis)
    cv2.imshow('analysed',medic)

    _, stDev = cv2.meanStdDev(mod)
    print (str(stDev))

    sdThresh = cv2.getTrackbarPos('Standard Deviation Threshold Limit','settingWindow')


    #cv2.putText(frame3, "Standard Deviation - {}".format(round(stDev[0][0],0)), (70, 70), font, 1, (255, 0, 255), 1, cv2.LINE_AA)
    display = frame3




    if stDev > sdThresh:
        #_, contours, hierarchy = cv2.findContours(medic,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(display,contours,-1,(0,255,0),3)



        # computes the bounding box for the contour, and draws it on the frame,
        """for contour, hier in zip(contours, hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)

            cv2.rectangle(frame3, (x,y), (x+w,y+h), (255, 0, 0), 2)
"""
        num=num+1
        print(str(num) + "Motion detected.. Do something!!!")
        """if num==1:
            auto_email()"""




        _, contours, _ = cv2.findContours(medic, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:
            area = cv2.contourArea(contour)


            #cv2.drawContours(display, contour, -1, (0, 255, 0), 3)







    switch1 = cv2.getTrackbarPos(switch,'settingWindow')
    if switch1 ==1:
        cv2.imshow('settingWindow',img)
        print (str(sdThresh))
        cv2.imshow('LIVE STREAM',display)
    if switch1 ==0:
        cv2.destroyWindow('LIVE STREAM')

    key = cv2.waitKey(33)
    if  key== 27 or ord == 'q':
        break

cap.release()
out.release()
cv2.destroyAllWindows()
