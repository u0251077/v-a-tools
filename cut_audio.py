from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip, AudioFileClip

#vedio cut part
input_video_path = 'koko.mp3'
output_video_path = 'koko_10.wav'
with AudioFileClip(input_video_path) as video:
    new = video.subclip(0, 10)
    new.write_audiofile(output_video_path,fps=16000)
    
