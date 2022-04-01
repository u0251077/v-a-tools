#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2

#programming_fever
#play video in reverse mode using OpenCV python
import cv2   
cap = cv2.VideoCapture("a.mp4") 
check, vid = cap.read()
w = vid.shape[1]
h = vid.shape[0]

check = True 
frame_list = [] 

while(check == True): 
    check , vid = cap.read() 
    frame_list.append(vid) 
    
frame_list.pop() 
frame_list.reverse() 

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('re_a.mp4', fourcc, 30.0, (w, h))

for i in range(len(frame_list)):
    out.write(frame_list[i])  
    
cap.release()
out.release()

cv2.destroyAllWindows()
