from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip, AudioFileClip

#vedio cut part
input_video_path = 'in.mp4'
output_video_path = 'out_10.mp4'
with VideoFileClip(input_video_path) as video:
    new = video.subclip(0,10)
    new.write_videofile(output_video_path, audio_codec='aac')
    
    
    
