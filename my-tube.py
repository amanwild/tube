from pytube import Playlist
from moviepy.editor import *
import pytube
import os.path
from pytube import Playlist
import re
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

link = "https://youtube.com/playlist?list=PLU6SqdYcYsfLRq3tu-g_hvkHDcorrtcBK"
# link = "https://www.youtube.com/watch?v=Ai50j-9Ga7w&list=PLOZsCzXAYggsP7uRg3ZezVP7xR88plP7L"

def setTitle(Title):
      Title = re.sub('[^a-zA-Z.\d\s]', '', Title)
      print(" Video name : ", Title ,"\n")
      return Title
def getMax(reslist):
      print(reslist, " Full Resulation list (After append)")
      max_value = max(reslist)
      # index of max resulation
      max_indes = reslist.index(max_value)
      indices = [index for index, value in enumerate(reslist) if value == max_value]
      maxx = max(indices)
      print(maxx, "Selected max indice for video download")
      return maxx
def getMetadat(vid,reslist):
      for i in vid:
          tupl = list(i)
          strtupl = str(tupl[1])
          metalist = list(strtupl.split())
          tyvi = 'type="video">'
          if (metalist[-1] == tyvi):
              res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
              if res!="":
                  reslist.append(int(res))
      return reslist
def delete(a,v):
          os.remove(a)                             
          os.remove(v)                             
          print('Mixing Done')
def Download(videos,vid,maxx,Title):
      src =r"C:/vdo from tubee/"
      audio_index = (videos[len(vid)-1])
      ado = src+audio_index.default_filename
      upado = str(src+"a "+audio_index.default_filename)
      video_index = (videos[maxx])
      vdo = src+video_index.default_filename
      upvdo = str(src+"v "+video_index.default_filename)
      
      #audio path for cmd line
      asrc = str(PureWindowsPath(f"C:\\vdo from tubee\\"+"a "+audio_index.default_filename))
      #Video path for cmd line
      vsrc = str(PureWindowsPath(f"C:\\vdo from tubee\\"+"v "+video_index.default_filename))
      #OUTput path for cmd line
      osrc = (src+Title+".mp4")
      
      print(os.path.isfile(osrc))
      i=1
      #if File Already Exist
      while (os.path.exists(osrc)):
          print(osrc," :::::::::::Before Updation")
          osrc = src+Title+" MyTube_"+str(i)+" .mp4";
          i += 1;
          print(osrc,"  :::::::::::After Updation")
      print("Before file Audio :: "+str(ado)+"\n"+
            "Before file Video :: "+str(vdo)+"\n"+
            "Created file Audio :: "+str(upado)+"\n"+
            "Created file Video :: "+str(upvdo)+"\n"+
            "Src for A          :: "+str(asrc)+"\n"+
            "Src for V          :: "+str(vsrc)+"\n"+
            "Output Path        :: "+str(osrc)+"\n")
      try:
        audio_index.download(src)
        os.rename(ado, upado)
        print("\n Audio Successfully Download \n")
      except:  
            print("Audio Error")
      try:
        videos[maxx].download(src)
        os.rename(vdo,upvdo)
        print("\n Video Successfully Download \n")
        
        os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"')  
        if(os.path.exists(osrc)):
              delete(asrc,vsrc)
        else:
              print("Error")
      except:  
            
         print("video Error")
         
         videos[maxx+1].download(src)
         os.rename(vdo,upvdo)
         print("\n Video Successfully Download \n")
        
         os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"')  
         if(os.path.exists(osrc)):
              delete(asrc,vsrc)
        
            
            
try:
  youtube = Playlist(link)
  print(f'Playlist: {youtube.title}')
#length =len(youtube.video_urls)
#print(f'Playlist length: {length}')
  cond = 0
  
#where to start Downoad
  no =0
  
  vid = list(enumerate(youtube.videos))
  print("WELCOME to TUBE", vid in youtube.videos)
  for vid in youtube.videos:
      print(vid,"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
      if(str(youtube.videos[no])==str(vid)):
            cond = 1
      if cond:  
            Title = setTitle(vid.title)
            reslist = []#For Storing All Available resulation
            a = 0
            
            videos = vid.streams.all()
            
            vid = list(enumerate(videos))
            getMetadat(vid,reslist)
            maxx =getMax(reslist)
            Download(videos,vid,maxx,Title)

except:
  print("WELCOME to TUBE")
  youtube = YouTube(link)
  
  Title = setTitle(youtube.title)
  reslist = []#For Storing All Available resulation
  a = 0
  
  videos = youtube.streams.all()  # it give all formates
  vid = list(enumerate(videos))
  getMetadat(vid,reslist)
  
  maxx =getMax(reslist)
  # 
  Download(videos,vid,maxx,Title)

finally:
  print("You're Ready to Go")

