
import cv2

# A list of the paths of your videos
videos = ["video2.mp4", "video3.mp4"]
fps = 30
curr_v_t = cv2.VideoCapture(videos[0])
r, frame = curr_v_t.read()
w = frame.shape[1]
h = frame.shape[0]
# Create a new video
video = cv2.VideoWriter("new_video.avi", cv2.VideoWriter_fourcc(*"XVID"), fps, (w, h ))

# Write all the frames sequentially to the new video
for v in videos:
    print(v)
    curr_v = cv2.VideoCapture(v)
    while curr_v.isOpened():
        r, frame = curr_v.read()    # Get return value and curr frame of curr video
        if not r:
            break
        video.write(frame)          # Write the frame

video.release()                     # Save the video
