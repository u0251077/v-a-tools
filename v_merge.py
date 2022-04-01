#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2


cap = cv2.VideoCapture("./left.mp4")
cap2 = cv2.VideoCapture("./right.mp4")

ret, frame = cap.read()
ret2, frame2 = cap2.read()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('merge.mp4', fourcc, 30.0, (frame.shape[1]*2,frame.shape[0]))

while ret and ret2:
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()    
    
    image_h = cv2.hconcat([frame, frame2])    
    out.write(image_h)  
    
cap.release()
cap2.release()
out.release()
