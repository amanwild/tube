from pytube import Playlist
from moviepy.editor import *
import os.path
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

link = "https://www.youtube.com/watch?v=iSumr2i9BvQ"
# link = "https://www.youtube.com/watch?v=Ai50j-9Ga7w&list=PLOZsCzXAYggsP7uRg3ZezVP7xR88plP7L"


print("Welcome to MyTube")
try:
  youtube = Playlist(link)
  print(f'Playlist: {youtube.title}')
  length =len(youtube.video_urls)
  print(f'Playlist length: {length}')
  print(0)

  vid = list(enumerate(youtube.videos))
  for vid in youtube.videos:
      Title =(vid.title).replace('"','')
      Title = re.sub('[^a-zA-Z.\d\s]', '', Title)
      print("\n Video name : ", Title)
      
      reslist = []#For Storing All Available resulation
      a = 0
      def delete(a,v):
          os.remove(a)                             
          os.remove(v)                             
          print('Mixing Done')
      videos = vid.streams.all()
      vid = list(enumerate(videos))
    #   for i in vid:
    #       print(i,"  iiiiiiiiiiiiiiii")
      for i in vid:
          tupl = list(i)
          strtupl = str(tupl[1])
          metalist = list(strtupl.split())
          tyvi = 'type="video">'
          if (metalist[-1] == tyvi):
              res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
              if res!="":
                  reslist.append(int(res))
      print(reslist, " Full Resulation list (After append)")
      max_value = max(reslist)
      # index of max resulation
      max_indes = reslist.index(max_value)
      indices = [index for index, value in enumerate(reslist) if value == max_value]
      print(indices, "All max indices")
      maxx = max(indices)
      print(maxx, "Selected max indice for video download")
      
      src =r"D:/vdo from tube/"
      audio_index = (videos[len(vid)-1])
      ado = src+audio_index.default_filename
      upado = str(src+"a "+audio_index.default_filename)
      video_index = (videos[maxx])
      vdo = src+video_index.default_filename
      upvdo = str(src+"v "+video_index.default_filename)
      
      #audio path for cmd line
      asrc = str(PureWindowsPath(f"D:\\vdo from tube\\"+"a "+audio_index.default_filename))
      #Video path for cmd line
      vsrc = str(PureWindowsPath(f"D:\\vdo from tube\\"+"v "+video_index.default_filename))
      #OUTput path for cmd line
      osrc = (src+Title+".mp4")
      
      print(os.path.isfile(osrc))
      i=1
      print(osrc," :::::::::::Before name")
      while (os.path.exists(osrc)):
          osrc = src+Title+" MyTube_"+str(i)+" .mp4";
          i += 1;
      print(osrc,"  :::::::::::updated name")
      # print("Before file Audio :: "+str(ado)+"\n"+
      #     "Before file Video :: "+str(vdo)+"\n"+
      #     "Created file Audio :: "+str(upado)+"\n"+
      #     "Created file Video :: "+str(upvdo)+"\n"+
      #     "Src for A          :: "+str(asrc)+"\n"+
      #     "Src for V          :: "+str(vsrc)+"\n"+
      #     "Output Path        :: "+str(osrc)+"\n")
      
      audio_index.download(src)
      os.rename(ado, upado)
      print("\n Audio Successfully Download \n")
      videos[maxx].download(src)
      os.rename(vdo,upvdo)
      print("\n Video Successfully Download \n")
      
      os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"')  
      delete(asrc,vsrc)

except:
  youtube = YouTube(link)
  videos = youtube.streams.all()  # it give all formates
  vid = list(enumerate(videos))
  
  Title = re.sub('[^a-zA-Z.\d\s]', '', (youtube.title))
  print("\n Video Title : ", Title)
  reslist = []#For Storing All Available resulation
  
  def delete(a,v):
      os.remove(a)                              
      os.remove(v)                             
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
  max_value = max(reslist)
  # index of max resulation
  max_indes = reslist.index(max_value)
  indices = [index for index, value in enumerate(reslist) if value == max_value]
  maxx = max(indices)
  print(maxx, "Selected max indice for video download")
  
  src =r"D:/vdo from tube/"
  audio_index = (videos[len(vid)-1])
  ado = src+audio_index.default_filename
  upado = str(src+"a "+audio_index.default_filename)
  video_index = (videos[maxx])
  vdo = src+video_index.default_filename
  upvdo = str(src+"v "+video_index.default_filename)
  
  #audio path for cmd line
  asrc = str(PureWindowsPath(f"D:\\vdo from tube\\"+"a "+audio_index.default_filename))
  #Video path for cmd line
  vsrc = str(PureWindowsPath(f"D:\\vdo from tube\\"+"v "+video_index.default_filename))
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
  # print("Before file Audio :: "+str(ado)+"\n"+
  #       "Before file Video :: "+str(vdo)+"\n"+
  #       "Created file Audio :: "+str(upado)+"\n"+
  #       "Created file Video :: "+str(upvdo)+"\n"+
  #       "Src for A          :: "+str(asrc)+"\n"+
  #       "Src for V          :: "+str(vsrc)+"\n"+
  #       "Output Path        :: "+str(osrc)+"\n")
  
  audio_index.download(src)
  os.rename(ado, upado)
  print("\n Audio Successfully Download \n")
  videos[maxx].download(src)
  os.rename(vdo,upvdo)
  print("\n Video Successfully Download \n")
  
  os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"')  
  delete(asrc,vsrc)

else:
  print("You're Ready to Go")

