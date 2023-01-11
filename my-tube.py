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

link = "https://www.youtube.com/live/3OQAodOpZ08?feature=share"

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
      Title = re.sub('[^a-zA-Z.\d\s]', '', Title)
      print("\n Video name : ", Title)
      return Title
def getMax(reslist,attempt):
      global max_value
    #   max_value = "1080"
      print(reslist, " Full Resulation list (After append)")
      
    #   max_value = max(reslist)
    #   # index of max resulation
    #   max_indes = reslist.index(max_value)
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
      # if max_value>1080:
      #       indices = [index for index, value in enumerate(reslist) if value == max_value]
      maxx = max(indices)
      print(maxx, "Selected max indice for video download",max_value)
      
      
      return maxx
def getMetadat(vid,reslist,res_limit):
      for i in vid:
          tupl = list(i)
          strtupl = str(tupl[1])
          metalist = list(strtupl.split())
          tyvi = 'type="video">'
          if (metalist[-1] == tyvi):
              res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
              if res_limit :
                  if res=="" or res=="2160" or res=="1440" :
                      reslist.append(str(" 10"))
                  if res!="" and res!="2160" and res!="1440" :
                        reslist.append(int(res))
              else:
                   reslist.append(int(res))
      return reslist
def delete(a,v):
          os.remove(v)                             
          os.remove(a)                             
          print('Mixing Done')
          
def vd(src,vdo, upvdo):
    
    try:
        maxx =getMax(reslist,attempt=1)
        print("1st attempt Data video is download is start 1st attempt",max_value)
        videos[maxx].download(src)
        os.rename(vdo,upvdo)
        print("\n Video Successfully Download \n")
    except Exception as err:
        print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
        print("\n1 Video Download Error \n",max_value)
                 
        try:
            maxx =getMax(reslist,attempt=2)
            print("2nd atempt Data video to download ",max_value)
            
            videos[maxx].download(src)
            print("\n Video  Download \n")
            os.rename(vdo,upvdo)
            print("\n Video Successfully Download \n")
        except Exception as err:
            print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
            try:
                print("\n2 Video Download Error\n",max_value)
                
                maxx =getMax(reslist,attempt=3)
                print("3rd atempt Data video to download ",max_value)

                videos[maxx].download(src)
                print("\n Video  Download \n")
                os.rename(vdo,upvdo)
                print("\n Video Successfully Download \n")
                
            except Exception as err:
                print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
                try:
                  print("\n3 Video Download Error\n",max_value)
                  
                  maxx =getMax(reslist,attempt=4)
                  print("4rth atempt Data video to download ",max_value)
  
                  videos[maxx].download(src)
                  print("\n Video  Download \n")
                  os.rename(vdo,upvdo)
                  print("\n Video Successfully Download \n")
                  
                except Exception as err:
                  print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
                  try:
                    print("\n4 Video Download Error\n",max_value)

                    maxx =getMax(reslist,attempt=5)
                    print("5th atempt Data video to download ",max_value)

                    videos[maxx].download(src)
                    print("\n Video  Download \n")
                    os.rename(vdo,upvdo)
                    print("\n Video Successfully Download \n")
                    
                  except Exception as err:
                    print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
                    try:
                      print("\n5 Video Download Error\n",max_value)

                      maxx =getMax(reslist,attempt=6)
                      print("6th atempt Data video to download ",max_value)

                      videos[maxx].download(src)
                      print("\n Video  Download \n")
                      os.rename(vdo,upvdo)
                      print("\n Video Successfully Download \n")
                      
                    except Exception as err:
                      print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
                      print("\n6 Video Download Error\n",max_value)
            
   
      
def au(audio_index,src,ado, upado):
    
      try:
              print("Data audio  download is start ")
              audio_index.download(src)
              os.rename(ado, upado)
              print("\n Audio Successfully Download \n")
      except Exception as err:
          print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
          print("\n Audio Download Error\n")
      
      
      
      
def Download(videos,vid,maxx,Title,no):
      file = "vdo from tube"
      
      src =r"C:/"+file+"/"
    
      audio_index = (videos[len(vid)-1])
      a_index = audio_index.default_filename
      ado = src+a_index
      upado = str(src+"a "+a_index)
      
      v_index = (videos[maxx]).default_filename
      vdo = src+v_index
      upvdo = str(src+"v "+v_index)
      
      #audio path for cmd line
      asrc = str(PureWindowsPath(f"C:\\"+file+"\\"+"a "+a_index))
      #Video path for cmd line
      vsrc = str(PureWindowsPath(f"C:\\"+file+"\\"+"v "+v_index))
      #OUTput path for cmd line
      global osrc
      osrc = (src+no+" "+Title+"*")
      
      exist = 0    
      print("Before:"+no+" "+Title)
      for item in glob.glob(osrc):
          print("\n Already Exists",item,"\n")
          exist = 1
      
      if(exist):
          print("End")
          exit()
      else:
        print("already not Exist",osrc)
        
        osrc = (src+no+" "+Title+" "+str(max_value)+"p "+".mp4")
        print("Creating file :",os.path.isfile(osrc))
        # i=1
        #if File Already Exist
    #     while (os.path.exists(osrc)):
    #         print(osrc," :::::::::::Before Updation")
    #         osrc = src+Title+" MyTube_"+str(i)+" .mp4";
    #         i += 1;
    # #            print(osrc,"  :::::::::::After Updation")
    # #        print("Before file Audio :: "+str(ado)+"\n"+
    # #              "Before file Video :: "+str(vdo)+"\n"+
    # #              "Created file Audio :: "+str(upado)+"\n"+
    # #              "Created file Video :: "+str(upvdo)+"\n"+
    # #              "Src for A          :: "+str(asrc)+"\n"+
    # #              "Src for V          :: "+str(vsrc)+"\n"+
    # #              "Output Path        :: "+str(osrc)+"\n")
              
        try:
            if(os.path.isfile(upado)):
              print("",upado)
              print("\n Already Exist Audio \n")
            else:
              au(audio_index,src,ado, upado)
        except Exception as err:
            print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
            print("audio Download error ")
        try:
            if(os.path.isfile(upvdo)):
                print("\n Already Exist Video \n")
            else:
                vd(src,vdo, upvdo)
                
            
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
            if(os.path.isfile(osrc)):
                delete(asrc,vsrc)
            osrc = (src+no+" "+Title+" "+str(max_value)+"p "+".mp4")
            os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"') 
            if(os.path.isfile(osrc)):
                delete(asrc,vsrc)
        except Exception as err:
            print(f"Unexpected     ##################################### {err=}, {type(err)=}, Line no ={ err.__traceback__.tb_lineno}")
            print("File is not Available to combine")
  
      
      
            
print("Welcome to MyTube")

global src
global audio_index  
global no
global osrc
global Title 
global attempt
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
  
#   print(len(youtube.video_urls))

  print("WELCOME to TUBE", vid in youtube.videos)
  for vid in youtube.videos:
      print("here",vid)
      if((str(youtube.videos[no])==str(vid)) and (cond == 0)):
            cond = 1
      if cond:  
            # engine = pyttsx3.init()
            # engine.say("Thank you")
            # engine.runAndWait()
            
            Title = setTitle(vid.title)
            reslist = []#For Storing All Available resulation
            a = 0
            
            videos = vid.streams.all()
            vid = list(enumerate(videos))
            getMetadat(vid,reslist,res_limit)
            maxx = getMax(reslist,attempt=1)
            # maxx = 2
            no_ =str(no)
            print("before download")
            Download(videos,vid,maxx,Title,no_)
            no+=1
            print(no," Complete Out of ",(len(youtube.video_urls)))
except Exception as err:
  print(f"Unexpected     ##################################### {err=}, {type(err)=} ,Line no ={ err.__traceback__.tb_lineno}")
  
  yt = pytube.YouTube(link)
#   yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download("C:/vdo from tube")
  # yt = YouTube(link)
  # video = yt.streams.get_highest_resolution()
  # video.download("C:/vdo from tube")
  # print("here",yt)
  # print("",s)
  
  youtube = YouTube(link)
  Title = setTitle(youtube.title)
  reslist = []#For Storing All Available resulation
  no = 0
  res_limit = 0
  no_ =str(no)
  videos = youtube.streams.all()  # it give all formates
  vid = list(enumerate(videos))
  getMetadat(vid,reslist,res_limit)
  
  maxx =getMax(reslist,attempt=1)
  
  Download(videos,vid,maxx,Title,no_)

finally:
#   if ((no)<(len(youtube.video_urls))):
#       #   Thread(target = null).start()
#         print(no,"Incomplete",(len(youtube.video_urls)))
#   print(no,"complete",(len(youtube.video_urls)))
  
  engine = pyttsx3.init()
  engine.say("You're Ready to Go")
  engine.runAndWait()

