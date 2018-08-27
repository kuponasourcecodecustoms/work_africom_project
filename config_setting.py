import numpy as np
import cv2

from datetime import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



current_time=datetime.now()



def nothing(x):
    pass

def auto_email():
    fromaddr = "nigelvere@gmail.com"
    toaddr = "el17ntkv@leeds.ac.uk"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Motion Detected " + current_time.strftime("%Y-%m-%d-%H-%M")

    body = "Motion Detected"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "kuponandiye")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def distMap(frame1,frame2):
    frame1_32=np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(diff32[:,:,0]**2 + diff32[:,:,1]**2 + diff32[:,:,2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)
    return dist


def createGUI():
    img = np.zeros((300,512,3), np.uint8)*255
    img[:]=[0,0,255]
    cv2.namedWindow('settingWindow')
    cv2.createTrackbar('Standard Deviation Threshold Limit','settingWindow',4,10,nothing)

    switch = '0 :OFF\n1 :ON'
    cv2.createTrackbar(switch, 'settingWindow',0,1,nothing)


def updateGUI():
        pass
