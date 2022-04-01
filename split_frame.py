#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2


cap = cv2.VideoCapture("./input.mp4")


ret, frame = cap.read()

import time
c = 1
while ret:
    ret, frame = cap.read()

    st = "./data/frame"+str(c)+".png"
    c = c+1
    cv2.imwrite(st,frame)  
    
cap.release()
