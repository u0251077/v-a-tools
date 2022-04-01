import cv2
import numpy as np
import os
import time
from os.path import isfile, join
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))

    for i in range(len(files)):
        filename=pathIn + files[i]
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        if i ==0 :
            out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'XVID'), fps, size)                
        out.write(img)

    out.release()
def main():
    pathIn= './frame_folder/'
    pathOut = 'result.avi'
    fps = 30.0
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()
