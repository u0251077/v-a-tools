from moviepy.editor import *
in_v = '_.mp4'
out_v = '_ooo.mp4'

v = VideoFileClip(in_v)
v = v.without_audio()
v.write_videofile(out_v)
