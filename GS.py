# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 18:19:33 2020

@author: Asus
"""

import cv2
import numpy as np
cam = cv2.VideoCapture(0)
i=0
while i<100:
    i+=1
    _,replacefrm = cam.read()
replacefrm=cv2.resize(replacefrm,(1500,1500))
while True:
    _,frame = cam.read()
    frame=cv2.resize(frame,(1500,1500))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([64,74,0])
    upper_blue = np.array([111,255,251])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    maskinv = cv2.bitwise_not(mask)
    result = cv2.bitwise_and(frame,frame,mask=maskinv)
    coverimg = cv2.bitwise_and(replacefrm,replacefrm,mask=mask)
    finalimg = cv2.add(result,coverimg)
    cv2.imshow("image",finalimg)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cam.release()
cv2.destroyAllWindows()