from moviepy.editor import VideoFileClip,AudioFileClip
 


clip2 = AudioFileClip("Demo_speech_label_0_1.mp4")


clip2.write_audiofile("oou2-all.mp3",fps= 16000)
