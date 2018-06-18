# Competitive-Coding
Solutions to problems from different competitive coding sites


import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt  # Import
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os

def email(timestamp):
    img_data = open(timestamp, 'rb').read()
    #content = 'Intrusion alert!'

    msg = MIMEMultipart()
    msg['Subject'] = 'Intrusion alert!'
    msg['From'] = 'ayush1rko1tiwari@gmail.com'
    msg['To'] = 'ayushtiwariindia@gmail.com'

    text = MIMEText("There was an intruder in the lab! Check the attachment for details!")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(timestamp))
    msg.attach(image)

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()

    mail.login('ayush1rko1tiwari@gmail.com', 'password')

    mail.sendmail('ayush1rko1tiwari@gmail.com', 'ayushtiwariindia@gmail.com', msg.as_string())

    mail.close()




#%config InlineBackend.figure_format = 'svg'

options = {
    'model':'cfg/yolo.cfg',
    'load' : 'bin/yolo.weights',
    'threshold' : 0.6,
    'gpu' : 1.0
    }

tfnet = TFNet(options)

def yoloconfirm(img):
    person = 0
    result = tfnet.return_predict(img)
    for parameters in result:
        for j in parameters:
            if j == 'label' and parameters[j] == 'person':
                person = 1
    return person


from datetime import datetime
import pygame
import time #Importing the necessary libraries

alarm_audio = 'intrusion.mp3' #Choosing the audio for the alarm
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(alarm_audio) #Loading the audio file into the pygame object

fgbg = cv2.createBackgroundSubtractorMOG2()

print('YAAY')
def diffImg(t0, t1, t2): # Finding difference in frame 
    d1 = cv2.absdiff(t2 , t1)
    d2 = cv2.absdiff(t1 , t0)
    return cv2.bitwise_and(d1, d2) # If it persists


threshold = 500#125500
cam = cv2.VideoCapture(0) # Starts capturing live video feed
time.sleep(3)

winName = "Intrusion Detector"


t_minus = cv2.medianBlur(fgbg.apply(cv2. cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)), 15)
t = cv2.medianBlur(fgbg.apply(cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)), 15)
t_plus = cv2.medianBlur(fgbg.apply(cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)), 15) #gets the first three frames

timecheck = datetime.now().strftime('%Ss')
confirm = 0

while True:
    cv2.imshow('t', t)
    cv2.imshow('t_minus', t_minus)
    cv2.imshow('t_plus', t_plus)
    
    cv2.imshow('Intrusion Analysis', cam.read()[1]) #Displays the live video feed
    
    if cv2.countNonZero(diffImg(t_minus, t, t_plus)) > threshold and timecheck != datetime.now().strftime('%Ss'): #If frames have significant difference
        dimg = cam.read()[1]
        
        if confirm or yoloconfirm(dimg):
            confirm += 1
            s = datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg'
            cv2.imwrite(s, dimg) #Save the file along with the time and the date as the file name
##            if confirm == 1:
##                email(s)
            pygame.mixer.music.play() #Sound the alarm
        
    timecheck = datetime.now().strftime('%Ss')

    t_minus = t
    t = t_plus
    t_plus = cv2.medianBlur(fgbg.apply(cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)), 15) # Get the next frames

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break



##img = cv2.imread('ayush.jpg')

