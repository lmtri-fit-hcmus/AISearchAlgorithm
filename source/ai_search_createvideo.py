from more_itertools import only
from moviepy.editor import *
from os import listdir
from os.path import isfile, join

def createVideo(videoName):
    mypath = "tmp_image"
    onlyfiles = []
    for i in listdir(mypath):
        onlyfiles.append(mypath +'/'+i)
    onlyfiles.sort(key=lambda x: os.path.getmtime(x))
    clips = []

    for i in onlyfiles:
        if i[i.find('.')-1] != '_':
            clip =  ImageClip(i).set_duration(0.009)
        else:
            clip =  ImageClip(i).set_duration(0.03)
            #print(i)
        clips.append(clip)
        os.remove(i)


    video_clip = concatenate_videoclips(clips, method='compose')
    video_clip.write_videofile("output/"+videoName, fps=24, remove_temp=True, codec="libx264", audio_codec="aac")