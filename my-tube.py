from moviepy.editor import *
import os.path

from os.path import exists
from random import randrange
from pathlib import Path
import os
from pathlib import Path, PureWindowsPath
import subprocess
import ffmpeg
import moviepy.editor as mpe
from pytube import YouTube
import random
import string

link = "https://www.youtube.com/watch?v=n5vLzoLEUhc"
youtube = YouTube(link)
Title =(youtube.title).replace('"','')
Title =Title.replace('|','')
print("\n Title : ", Title)


# videos =youtube.streams.filter(only_video=True)#it give all formates
videos = youtube.streams.all()  # it give all formates
vid = list(enumerate(videos))
reslist = []#For Storing All Available resulation
a = 0
def delete(a,v):
    os.remove(a)                             
    os.remove(v)                             
    print('Mixing Done')
    
for i in vid:
    print(i)
    
for i in vid:
    # Geting all metadata form vid
    tupl = list(i)
    strtupl = str(tupl[1])
    metalist = list(strtupl.split())

    tyvi = 'type="video">'
    if (metalist[-1] == tyvi):
        res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
        if res!="":
            reslist.append(int(res))
        
print(reslist, " Full Resulation list (After append)")
# maxx = reslist.index(max( int(i) for i in reslist))

# max resulation
max_value = max(reslist)
# index of max resulation
max_indes = reslist.index(max_value)
indices = [index for index, value in enumerate(reslist) if value == max_value]
print(indices, "All max indices")
maxx = max(indices)
print(maxx, "Selected max indice for video download")
code = ''.join((random.choice(string.ascii_lowercase) for x in range(3))) # run loop until the define length
print(code)

src =r"D:/vdo from tube/"
audio_index = (videos[len(vid)-1])
ado = src+audio_index.default_filename
upado = src+str(code)+" a "+audio_index.default_filename

video_index = (videos[maxx])
vdo = src+video_index.default_filename
upvdo = src+str(code)+" v "+video_index.default_filename

#audio path for cmd line
asrc = PureWindowsPath(f"D:\\vdo from tube\\"+str(code)+" a "+audio_index.default_filename)
#Video path for cmd line
vsrc = PureWindowsPath(f"D:\\vdo from tube\\"+str(code)+" v "+video_index.default_filename)
#OUTput path for cmd line
osrc = (src+Title+".webm")

print('D://vdo from tube//STRUGGLE HARD 😎🔥WhatsApp Status shorts Billionaire Attitude Status🔥motivation quotes.webm')

print(os.path.isfile(osrc))
i=1
print(osrc," :::::::::::Before name")
while (os.path.exists(osrc)):
    print("\n Video Exist\n")
    osrc = src+Title+str(i)+".mp4";
    i += 1;
    print(osrc,"  :::::::::::updated name")

audio_index.download(src)
os.rename(ado, upado)
print("\n Audio Successfully Download \n")

videos[maxx].download(src)
os.rename(vdo,upvdo)
print("\n Video Successfully Download \n")

print("Created file Audio :: "+str(upado)+"\n"+
      "Created file Video :: "+str(upvdo)+"\n"+
      "Src for A          :: "+str(asrc)+"\n"+
      "Src for V          :: "+str(vsrc)+"\n"+
      "Output Path        :: "+str(osrc)+"\n")



# fname = (f"{video_index.default_filename} vioindex file name")
# print(src+" scr")
# print(fname+" fname")
# print(osrc+" oscr")
# osrc = Path(f"{src}{fname}")

# print(os.path.isfile(f"D:/vdo from tube/STRUGGLE HARD 😎🔥WhatsApp Status shorts Billionaire Attitude Status🔥motivation quotes.webm"))

# if osrc.is_file(str(fname)):
#     print("\n  if

print("\n NOT  Exist\n")

# cmd = '-i "ring.webm" -i "rings.webm" -c copy "outpfut.mkv"'
Title=str(Title)
os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"')  



delete(asrc,vsrc)



