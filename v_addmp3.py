from moviepy.editor import *
videoclip = VideoFileClip("A.mp4")
audioclip = AudioFileClip("B.wav")

new_audioclip = CompositeAudioClip([audioclip])
videoclip.audio = new_audioclip
videoclip.write_videofile("A_B.mp4")
