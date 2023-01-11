from pytube import Playlist
from moviepy.editor import *
import os.path
import re
from os.path import exists
from random import randrange
from playsound import playsound

from pathlib import Path
import os
from pathlib import Path, PureWindowsPath
# import subprocess
import threading
from threading import Thread
import ffmpeg
import moviepy.editor as mpe
from pytube import YouTube
import pyttsx3

link = "https://www.youtube.com/live/adw2FHlvgmk?feature=share"

def setTitle(Title):
      Title = re.sub('[^a-zA-Z.\d\s]', '', Title)
      print("\n Video name : ", Title)
      return Title
def delete(a,v):
          os.remove(a)                             
          os.remove(v)                             
          print('Mixing Done')
          
def vd(maxx,src,vdo, upvdo):
      try:
          if os.path.exists(upvdo):
              print("Data video is present ")
          else:
              print("Data video is download is start")
              videos[maxx].download(src)
              os.rename(vdo,upvdo)
              print("\n Video Successfully Download \n")
      except:
          print("\n Video Download Error\n")
      
def au(audio_index,src,ado, upado):
      try:
          if os.path.exists(upado):
              print("Data audio is present ")
          else:
              print("Data audio  download is start ")
              audio_index.download(src)
              os.rename(ado, upado)
              print("\n Audio Successfully Download \n")
      except:
          print("\n Audio Download Error\n")
      
      
      
      
def Download(videos,vid,maxx,Title):
      file = "vdo from tube"
      src = str(f"C:/"+file+"/")
      audio_index = (videos[len(vid)-1])
      ado = src+audio_index.default_filename
      upado = str(src+"a "+audio_index.default_filename)
      video_index = (videos[maxx])
      vdo = src+video_index.default_filename
      upvdo = str(src+"v "+video_index.default_filename)
      
      osrc = (src+Title+".mp4")
      if(os.path.exists(osrc)):
          print("already Exist",osrc)
          pass
      else:
        # try:
        #     # au(audio_index,src,ado, upado)
        # except :
        #     print("audio Download error ")
        try:
            vd(maxx,src,vdo, upvdo)
        except :
            print("video Download error 1")

        try:
            if(os.path.exists(upvdo)):
                print("recheck Done ")
            else:
                try:
                     maxx = 2  
                     vd(maxx,src,vdo, upvdo)
                except :
                     print("Error last")
        except :
            print("Error")
  
      
      
            
print("Welcome to MyTube")
try:
  youtube = Playlist(link)
  print(f'Playlist: {youtube.title}')
  #limit for resuletion under 1080 
  res_limit = 1
#where to start Downoad
  cond = 0
  no =0
#   len(playlist.video_urls)
  vid = list(enumerate(youtube.videos))
  print('Number of videos in playlist: %s' % len(youtube.video_urls))
  
#   print(len(youtube.video_urls))

  print("WELCOME to TUBE", vid in youtube.videos)
  for vid in youtube.videos:
      
      print(vid,"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
      if((str(youtube.videos[no])==str(vid)) and (cond == 0)):
            cond = 1
      if cond:  
            print(no," Complete Out of ",(len(youtube.video_urls)))
            engine = pyttsx3.init()
            engine.say("Thank you")
            engine.runAndWait()
            Title = setTitle(vid.title)            
            print(no," After title")
            videos = vid.streams.all()
            vid = list(enumerate(videos))
            maxx = 3
            print(no," before download ")
            Download(videos,vid,maxx,Title)
            print(no," after download ")
            no+=1
except:
  
  print(no,"complete",(len(youtube.video_urls))," Errpr")

finally:
  if ((no)<(len(youtube.video_urls))):
        print(no,"Incomplete",(len(youtube.video_urls)))
  print(no,"complete",(len(youtube.video_urls)))
  
  engine = pyttsx3.init()
  engine.say("You're Ready to Go")
  engine.runAndWait()

