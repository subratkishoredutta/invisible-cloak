# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:19:33 2020

@author: Asus
"""
## 'pip install opencv-python'
## 'pip install numpy'

import cv2
import numpy as np

cam = cv2.VideoCapture(0)


i=0

while i<10:
    i+=1
    _,background= cam.read()
    #background=cv2.imread("DSCC.png")

    
replacefrm=cv2.resize(background,(1000,1000))


while True:
    _,frame = cam.read()
    frame=cv2.resize(frame,(1000,1000))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = np.array([64,74,0])
    upper_blue = np.array([111,255,251])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    maskinv = cv2.bitwise_not(mask)
    
    IL = cv2.bitwise_and(frame,frame,mask=maskinv)
    
    CL = cv2.bitwise_and(replacefrm,replacefrm,mask=mask)
   
    finalimg = cv2.add(IL,CL)
    
    cv2.imshow("image",finalimg)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
       
cam.release()
cv2.destroyAllWindows()