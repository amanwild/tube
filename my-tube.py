from pytube import Playlist
from moviepy.editor import *
import os.path
import re
from os.path import exists
from random import randrange
from playsound import playsound
import glob
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
import pytube

import random
import string

# link = "https://youtube.com/playlist?list=PLFr_jkwUp0hhm1lR1TSdgESOfoyLQR3t2"
link = "https://youtube.com/playlist?list=PLT9miexWCpPXtHIZmS_Yn1IGpgcEoVqZr"
# https://www.youtube.com/live/-gqNTmPv66s?feature=share
# youtube = pytube.YouTube(link)  
# video = youtube.streams.first()  
# print("here",video)
# try:
#   video.download("C:/vdo from tube")  
# except Exception as err:
#     print(f"Unexpected     ##################################### {err=}, {type(err)=}")

# yt = pytube.YouTube(link)
# #   yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("C:/vdo from tube")
# yt = YouTube(link)
# video = yt.streams.get_highest_resolution()
# video.download("C:/vdo from tube")
# link = "https://youtube.com/shorts/AGTTnZAJYTM?feature=share"

url = link
def setTitle(Title):
  try:
    Title = re.sub('[^a-zA-Z\d\s]', '', Title)
    print("\n Video name : ", Title)
    return Title
  except:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
def checkTitle(Title):
  try:
    Title = re.sub('[^a-zA-Z\d\s]', '*', Title)
    print("\n Check name : ", Title)
    return Title
  except:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
def getMax(reslist,attempt):
  global max_value
  global u_maxx
  global meen  
  try:  
      #   max_value = "1080"
    print(reslist, " Full Resulation list (After append)")
    
    max_value = max(reslist)
    # index of max resulation
    # max_indes = reslist.index(max_value)
    # Removing duplicates from the list
    lists = list(set(reslist))
    # Sorting the  list
    lists.sort()
    # Printing the second last element
    
    if (attempt== 1):
      print("1 largest element is:", lists[-1])
      max_value = lists[-1]
    if (attempt== 2):
      print("2 largest element is:", lists[-2])
      max_value = lists[-2]
    if (attempt== 3):
      print("3 largest element is:", lists[-3])
      max_value = lists[-3]
    if (attempt== 4):
      print("4 largest element is:", lists[-4])
      max_value = lists[-4]
    if (attempt== 5):
      print("5 largest element is:", lists[-5])
      max_value = lists[-5]
    if (attempt== 6):
      print("6 largest element is:", lists[-6])
      max_value = lists[-6]
  
    
    indices = [index for index, value in enumerate(reslist) if value == max_value]
    if (attempt== 1):
          u_maxx = max(indices)
    maxx = max(indices)
    meen = min(indices)
    print(maxx,"or",meen, "Selected max indice for video download",max_value)
    
    
    return maxx
  except:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
    
def getMetadat(vid,reslist,res_limit):
  try:
    print("\nGetting metadata (resulation list BY getmetadata)")
    for i in vid:
      tupl = list(i)
      strtupl = str(tupl[1])
      metalist = list(strtupl.split())
      tyvi = 'type="video">'
      if (metalist[-1] == tyvi):
        res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
        if res_limit :
          if res=="" or res=="2160" or res=="1440" :
            reslist.append(int(10))
          if res!="" and res!="2160" and res!="1440" :
            reslist.append(int(res))
        else:
            reslist.append(int(res))
    return reslist
  except:
        print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
def delete(a,v):
  try:    
    os.remove(v)                             
    os.remove(a)                             
    print('Mixing Done')
  except:
        print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
  
          
def vd():
  global upvdo
  global v_index
  global maxx
  
  try:

    for attempt in range(10):
      try:
        maxx =getMax(reslist,attempt=attempt+1)
        print(str(attempt+1)," attempt with ",maxx," Resulation",max_value)
        videos[maxx].download(src)
        print("\n Video Successfully Download \n")
        v_index = (videos[u_maxx]).default_filename
        vdo = src+v_index
        upvdo = str(src+"v "+v_index)
        os.rename(vdo,upvdo)
        attempt =10
        break
      except Exception as err:
        print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
        print(str(attempt+1)," Video Download Error \n",max_value)
        try:
          print(str(attempt+1)," attempt with ",meen," Resulation",max_value)
          videos[meen].download(src)
          print("\n Video Successfully Download \n")
          v_index = (videos[u_maxx]).default_filename
          vdo = src+v_index
          upvdo = str(src+"v "+v_index)
          os.rename(vdo,upvdo)
          attempt =10
          break
        except Exception as err:
          print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
          print(str(attempt+1)," Video Download Error \n",max_value)
          
        

        
  except:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
 
   
      
def au(audio_index,ado, upado):
    
      try:
          print("Data audio  download is start ")
          audio_index.download(src)
          os.rename(ado, upado)
          print("\n Audio Successfully Download \n")
      except Exception as err:
          print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
          print("\n Audio Download Error\n")
      
      
      
      
def Download(videos,vid,Title,no):
   
  audio_index = (videos[len(vid)-1])
  a_index = audio_index.default_filename
  ado = src+a_index
  upado = str(src+"a "+a_index)
  
  
  #audio path for cmd line
  asrc = str(PureWindowsPath(f"C:\\"+file+"\\"+"a "+a_index))
  #Video path for cmd line
  
  #OUTput path for cmd line
  # print("Temporary Video and Audio name\n",v_index,"\n",a_index,"\n",asrc,"\n",vsrc)
  
  
  
  
  
  # i=1
  #if File Already Exist
 #    while (os.path.exists(osrc)):
 #        print(osrc," :::::::::::Before Updation")
 #        osrc = src+Title+" MyTube_"+str(i)+" .mp4";
 #        i += 1;
 ##            print(osrc,"  :::::::::::After Updation")
 ##        print("Before file Audio :: "+str(ado)+"\n"+
 ##              "Before file Video :: "+str(vdo)+"\n"+
 ##              "Created file Audio :: "+str(upado)+"\n"+
 ##              "Created file Video :: "+str(upvdo)+"\n"+
 ##              "Src for A          :: "+str(asrc)+"\n"+
 ##              "Src for V          :: "+str(vsrc)+"\n"+
 ##              "Output Path        :: "+str(osrc)+"\n")
        
  try:
    if(os.path.isfile(upado)):
      print("",upado)
      print("\n Already Exist Audio \n")
    else:
      au(audio_index,ado, upado)
  except Exception as err:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
    print("audio Download error ")
  try:
    upvdo = (src+"*v*"+Title+"*")

    exist = 0    
    for item in glob.glob(upvdo):
      print("\nAlready Exists :",upvdo)
      exist = 1
    if(exist):
      print("\n Video Download Skipped \n")
      upvdo
      global v_index
      global maxx
      
      try:
        maxx =getMax(reslist,attempt=1)
        v_index = (videos[u_maxx]).default_filename
        upvdo = str(src+"v "+v_index)
            
      except Exception as err:
        print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
      pass
    else:
      vd()
          
      
  except Exception as err:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
    try:
      if(os.path.isfile(upvdo)):
        print("recheck Done v file is present ")
      else:
        print("v file is'nt present ,starting to download v file ")
      # pass
        # try:
        #     # osrc = (src+no+" "+Title+" "+str(max_value)+"p "+".mp4")
        #     # try:
        #     #   print("download v file 2nd attempt ")  
        #     #   maxx=2
        #     #   vd(maxx,src,vdo, upvdo)
        #     # except:
        #     #   print("download v file 3rd attempt ")
        #     #   maxx=1
        #     #   vd(maxx,src,vdo, upvdo)
        #     # print("rejoining 2nd attempt ")
        #     # os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"') 
            
        # except :
        #     print("Error last")
    except Exception as err:
      print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
      pass
    print("video Download error 1")
  try:
    # osrc = str(src+no+" "+str(max_value)+v_index)
    # v_index = (videos[u_maxx]).default_filename
    try:
      osrc = (src+no+" ("+str(max_value)+"p) "+v_index)
    except Exception as err:
      print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
      osrc = (src+no+" ("+str(max_value)+"p) "+Title+".mp4")
    print("Creating file :",osrc)
    vsrc = str(PureWindowsPath(f"C:\\"+file+"\\"+"v "+v_index))
    if(os.path.isfile(osrc)):
      delete(asrc,vsrc)
    # osrc = (src+no+" "+Title+" "+str(max_value)+"p "+".mp4")
    os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"') 
    if(os.path.isfile(osrc)):
      delete(asrc,vsrc)
    # os.rename(osrc, upado)
  except Exception as err:
    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
    print("File is not Available to combine")
  
      
      
            
def Processing(vid,no):
  Welcome()
  global no_
  no_ = no
  Title = checkTitle(vid.title)
  no_ =str(no)
 
  # osrc = (src+no_+"*"+Title+"*")
  osrc = (src+no_+"*"+Title+"*")

  exist = 0
  for item in glob.glob(osrc):
    print("\nAlready Exists :",no_,vid.title)
    exist = 1
    break

  if(exist):
    print("Downloading is Skiped \n")
    no+=1
    pass
  else:
    print("already not Exist",osrc)
    

    try:
      global videos
      videos = vid.streams.all()  # it give all formates
      vid = list(enumerate(videos))
      getMetadat(vid,reslist,res_limit)
      # maxx =getMax(reslist,attempt=1)
      Download(videos,vid,Title,no_)
    except Exception as err:
      print(f"Unexpected     ##################################### {err=}, {type(err)=} ,Line no ={ err.__traceback__.tb_lineno}")
      
  

def Welcome():
  global src
  global audio_index  
  
  global reslist
  reslist = []
  global osrc
  global file
  global Title 
  global max_value
  global res_limit
  res_limit = 0
  max_value ="0"
  global attempt
  file = "vdo from tube"
  src =r"C:/"+file+"/" 
  
try:
  print("Welcome to MyTube")
  youtube = Playlist(link)
  print(f'Playlist: {youtube.title}')
  #limit for resuletion under 1080 
  
#where to start Downoad
#   len(playlist.video_urls)
  vid = list(enumerate(youtube.videos))
  
  cond = 0
  global no
  no=0

#   print(len(youtube.video_urls))

  # print("WELCOME to TUBE", vid in youtube.videos)
  for vid in youtube.videos:
      # print("here",vid)
      if((str(youtube.videos[no])==str(vid)) and (cond == 0)):
            cond = 1
      if cond:  
            # engine = pyttsx3.init()
            # engine.say("Thank you")
            # engine.runAndWait()
            Processing(vid,no)
            print(no," Complete Out of ",(len(youtube.video_urls)))
            no+=1
except Exception as err:
  try:
    print(f"Unexpected     ##################################### {err=}, {type(err)=} ,Line no ={ err.__traceback__.tb_lineno}")
    print("Entering in Special Video Downloding")
    yt = pytube.YouTube(link)
    vid = YouTube(link)
   #For Storing All Available resulation
    
    Processing(vid,no=0)
   
  except Exception as err:
    print("Exit from Code")
    print(f"Unexpected     ##################################### {err=}, {type(err)=} ,Line no ={ err.__traceback__.tb_lineno}")

  finally:
  #   if ((no)<(len(youtube.video_urls))):
  #       #   Thread(target = null).start()
  #         print(no,"Incomplete",(len(youtube.video_urls)))
  #   print(no,"complete",(len(youtube.video_urls)))
    
    engine = pyttsx3.init()
    engine.say("You're Ready to Go")
    engine.runAndWait()

