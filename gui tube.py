# from tkinter import *
# from pytube import YouTube
# from tkinter.font import BOLD
# from pytube import Playlist
# from moviepy.editor import *
# import os.path
# import re
# from os.path import exists
# from random import randrange
# from playsound import playsound

# from pathlib import Path
# import os
# from pathlib import Path, PureWindowsPath
# # import subprocess
# import threading
# from threading import Thread
# import ffmpeg
# import moviepy.editor as mpe
# from pytube import YouTube
# import pyttsx3


# import random
# import string

    
# def select_color():
#     global i ,limit
#     i=int(var.get())
#     limit =i
# ##################################################IT USED FOR BASIC PROCCESSING #############################################################

# def stop():
#     pass
# def web_cam():
#    pass



# def setTitle(Title):
#       Title = re.sub('[^a-zA-Z.\d\s]', '', Title)
#       print("\n Video name : ", Title)
#       return Title
# def getMax(reslist):
#       print(reslist, " Full Resulation list (After append)")
#       global max_value
#       max_value = max(reslist)
#       # index of max resulation
#       max_indes = reslist.index(max_value)
#       indices = [index for index, value in enumerate(reslist) if value == max_value]
#       # if max_value>1080:
#       #       indices = [index for index, value in enumerate(reslist) if value == max_value]
#       maxx = max(indices)
#       print(maxx, "Selected max indice for video download",max_value)
#       return maxx
# def getMetadat(vid,reslist,res_limit):
#       for i in vid:
#           tupl = list(i)
#           strtupl = str(tupl[1])
#           metalist = list(strtupl.split())
#           tyvi = 'type="video">'
#           if (metalist[-1] == tyvi):
#               res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
#               if res_limit :
#                   if res=="" or res=="2160" or res=="1440" :
#                       reslist.append(str(" 10"))
#                   if res!="" and res!="2160" and res!="1440" :
#                         reslist.append(int(res))
#               else:
#                    reslist.append(int(res))
#       return reslist
# def delete(a,v):
#           os.remove(v)                             
#           os.remove(a)                             
#           print('Mixing Done')
          
# def vd(maxx,src,vdo, upvdo):
#       try:
#           if os.path.exists(upvdo):
#               print("Data video is present ")
#           else:
#               try:
#                   print("Data video is download is start")
#                   videos[maxx].download(src)
#                   os.rename(vdo,upvdo)
#                   print("\n Video Successfully Download \n")
#               except:
#                   os.remove(src) 
#                   try:
#                       print("2nd atempt Data video to download ")
#                       maxx = maxx-1  
#                       vd(maxx,src,vdo, upvdo)
#                   except :
#                       print("3rd atempt Data video to download ")
#                       maxx = maxx-2 
#                       vd(maxx,src,vdo, upvdo)
                  
                
#       except:
#           print("\n Video Download Error\n")
      
# def au(audio_index,src,ado, upado):
#       try:
#           if os.path.exists(upado):
#               print("Data audio is present ")
#           else:
#               print("Data audio  download is start ")
#               audio_index.download(src)
#               os.rename(ado, upado)
#               print("\n Audio Successfully Download \n")
#       except:
#           print("\n Audio Download Error\n")
      
      
      
      
# def Download(videos,vid,maxx,Title,no,max_value):
#       file = "vdo from tube"
#       src =r"C:/"+file+"/"
    
#       audio_index = (videos[len(vid)-1])
#       a_index = audio_index.default_filename
#       ado = src+a_index
#       upado = str(src+"a "+a_index)
      
#       v_index = (videos[maxx]).default_filename
#       vdo = src+v_index
#       upvdo = str(src+"v "+v_index)
      
#       #audio path for cmd line
#       asrc = str(PureWindowsPath(f"C:\\"+file+"\\"+"a "+a_index))
#       #Video path for cmd line
#       vsrc = str(PureWindowsPath(f"C:\\"+file+"\\"+"v "+v_index))
#       #OUTput path for cmd line
#       osrc = (src+no+" "+Title+" "+str(max_value)+"p "+".mp4")
#       if(os.path.exists(osrc)):
#           print("already Exist",osrc)
#           pass
#       else:
#         print("new file :",os.path.isfile(osrc))
#         # i=1
#         #if File Already Exist
#     #     while (os.path.exists(osrc)):
#     #         print(osrc," :::::::::::Before Updation")
#     #         osrc = src+Title+" MyTube_"+str(i)+" .mp4";
#     #         i += 1;
#     # #            print(osrc,"  :::::::::::After Updation")
#     # #        print("Before file Audio :: "+str(ado)+"\n"+
#     # #              "Before file Video :: "+str(vdo)+"\n"+
#     # #              "Created file Audio :: "+str(upado)+"\n"+
#     # #              "Created file Video :: "+str(upvdo)+"\n"+
#     # #              "Src for A          :: "+str(asrc)+"\n"+
#     # #              "Src for V          :: "+str(vsrc)+"\n"+
#     # #              "Output Path        :: "+str(osrc)+"\n")

#         try:
#             au(audio_index,src,ado, upado)
#         except :
#             print("audio Download error ")
#         try:

#             vd(maxx,src,vdo, upvdo)
#         except :
#             print("video Download error 1")


#         try:
#             os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"') 
#             delete(asrc,vsrc) 
#         except:
#             print("File is not Available to combine")
#             try:
#                 if(os.path.exists(upvdo)):
#                     print("recheck Done v file is present ")
#                 else:
#                     print("v file is'nt present ,starting to download v file ")
#                     # pass
#                     try:
#                         max_value = reslist[2]
#                         osrc = (src+no+" "+Title+" "+str(max_value)+"p "+".mp4")
#                         maxx=2
#                         vd(maxx,src,vdo, upvdo)
#                         maxx=1
#                         vd(maxx,src,vdo, upvdo)
                        
#                         print("rejoining 2nd attempt ")
#                         os.system(f'ffmpeg -i "{vsrc}" -i "{asrc}" -c copy "{osrc}"') 
#                         if(os.path.exists(osrc)):
#                             delete(asrc,vsrc)
#                     except :
#                         print("Error last")
#             except :
#                 print("Error")
  
      
      
            
# print("Welcome to MyTube")

# def downloader():
#     print("here1")
#     url=str(link.get())
#     print("here2")
#     try:
#       print("here3")
#       youtube = Playlist(url)
#       print(f'Playlist: {youtube.title}')
#       print("here4")
#       #limit for resuletion under 1080 
#       res_limit = 1
#     #where to start Downoad
#       cond = 0
#       no =0
#     #   len(playlist.video_urls)
#       vid = list(enumerate(youtube.videos))
#       global reslist
#       global videos
#       global videos
#       global total
#       noo= str(no)
#       total=str(len(youtube.video_urls))
#       aman = Label(text =f"{noo} Complete" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
#       aman.grid(row  = 0, column=0,sticky= N)
#       aman = Label(text =f"Out of {total}" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
#       aman.grid(row  = 1, column=0,sticky= S)
#       total = str(len(youtube.video_urls))
#     #   print(len(youtube.video_urls))
    
#       print("WELCOME to TUBE", vid in youtube.videos)
#       for vid in youtube.videos:
               
#           if((str(youtube.videos[no])==str(vid)) and (cond == 0)):
#                 cond = 1
#           if cond:  
#                 # engine = pyttsx3.init()
#                 # engine.say("Thank you")
#                 # engine.runAndWait()
#                 Title = setTitle(vid.title)
#                 reslist = []#For Storing All Available resulation
#                 a = 0
                
#                 videos = vid.streams.all()
#                 vid = list(enumerate(videos))
#                 getMetadat(vid,reslist,res_limit)
#                 maxx = getMax(reslist)
#                 # maxx = 2
#                 no_ =str(no)
#                 print("before download")
#                 Download(videos,vid,maxx,Title,no_,max_value)
#                 no+=1
#                 print(no," Complete Out of ",(len(youtube.video_urls)))
#     except:
#       print("here5")
#       youtube = YouTube(url)
#       print("here6")
#       Title = setTitle(youtube.title)
#       print("here7")
#       reslist = []#For Storing All Available resulation
#       no = 0
#       res_limit = 1
#       no_ =str(no)
#       videos = youtube.streams.all()  # it give all formates
#       vid = list(enumerate(videos))
#       getMetadat(vid,reslist,res_limit)
      
#       maxx =getMax(reslist)
      
#       Download(videos,vid,maxx,Title,no_,max_value)
    
#     finally:
#         try:
#             if ((no)<(len(youtube.video_urls))):
#                 #   Thread(target = null).start()
#                   print(no,"Incomplete",(len(youtube.video_urls)))
#             print(no,"complete",(len(youtube.video_urls)))
#         except:
#             pass
#         finally:
#             engine = pyttsx3.init()
#             engine.say("You're Ready to Go")
#             engine.runAndWait()
    

# ###################################IT USED FOR MAIN FUNCTION INITIALIZATION PROCCESSING ###################################################################

# __name__ == "__main__"
# project = Tk()
# i = 0
# # project.iconbitmap("Custom-Icon-Design-Mono-General-2-Search.ico")
# bg_color = '#5DADE2'
# project.geometry("500x800")
# project.minsize(400,200)
# project.configure(bg=bg_color )
# project.title("Object Detection Project")    
# suc="Successfully Downloaded"
# global no 
# no = ""
# total=""
# aman = Label(text =f"{no} Complete" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
# aman.grid(row  = 0, column=0,sticky= N)
# aman = Label(text =f"Out of {total}" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
# aman.grid(row  = 1, column=0,sticky= S)
# # aman = Label(text ="Complete Out of" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
# # aman.grid(row  = 0, column=0,sticky= N)
    

# ##################################################IT USED FOR FRAMING ###################################################################

# f0 = Frame(project,bg = ('#CCCCFF'), borderwidth=3,relief=SUNKEN)
# f0.grid(row=2, column=0, sticky=" ",)
# f0.grid_columnconfigure(0, weight=1)

# f01 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
# f01.grid(row = 0,column = 0,columnspan = 2,padx =15,pady= 25)

# f02 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
# f02.grid(row = 1,column = 0,columnspan = 2,padx =15,pady=2)

# f1 = Frame(f0,bg = "#BB8FCE")
# f1.grid(row = 2,column = 0,padx =15,pady= 25)
# f11 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=SUNKEN)
# f11.grid(row = 2,column = 1,padx =5,pady= 25)

# f2 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
# f2.grid(row = 1,column = 0,padx =15,pady= 25)

# f3 = Frame(f0,bg = "#BB8FCE", borderwidth=3,relief=GROOVE)
# f3.grid(row = 3,rowspan = 3,column = 0 ,columnspan = 4,padx =40,pady= 25)

# f4 = Frame(f0,bg = "#BB8FCE", borderwidth=3)
# f4.grid(row = 7,columnspan = 2,padx =15,pady= 25)

# ##################################################IT USED FOR BUTTONS ###################################################################

# processing = 0



# link = StringVar()
# link.set("")
# enter_link = Entry(f01,textvar = link,font = "lucida 15")
# enter_link.pack(fill=X,ipadx=50)

# process_web_cam = Button(f02,text ="Download",bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 20 bold", command =downloader, ) 






# process_web_cam.grid(padx = 5,pady = 5,ipadx =0,ipady = 0)
# process_stop = Button(f4,text ="Exit",bg = "#BB8FCE" ,fg = "red",font ="comicsansms 20 bold", command = stop, )
# process_stop.grid(padx = 5,pady = 5,ipadx = 0,ipady = 0)
# process_stop.bind('<Button-1>',quit)

# ##################################################IT USED FOR RADIO BUTTONS ###################################################################

# amans = Label(f3,text ="Choose Quality" ,font=("Arial", 15,BOLD), bg ='#CCCCFF' )
# amans.pack(padx = 15,pady = 5,ipadx =2)
# var = StringVar()
# var.set(0)    

# amans = Label(f1,text ="From Seq. no." ,font="comicsansms 15 bold" )
# amans.pack()

# no = StringVar()
# no.set("")
# enter_no = Entry(f11,textvar = no,font = "lucida 15")
# enter_no.pack()


























# radio = Radiobutton(f3,text="HIGH",bg = '#AACCFF',font ="comicsansms 15 bold",variable=var,value=(0),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)
# radio = Radiobutton(f3,text="LOW",bg = '#AACCFF',font ="comicsansms 15 bold",variable=var,value=(1),relief= RIDGE).pack(anchor="w",padx = 5,pady = 5,ipadx =0,ipady = 0)

# Button(f3,text="Apply",padx= 10,command = select_color, bg = "#BB8FCE" ,fg = "#FFFFFF",activebackground="#FFFFFF",activeforeground= "#BB8FCE",font ="comicsansms 15 bold").pack(padx = 5,pady = 5,ipadx = 0,ipady = 0)
# project.grid_rowconfigure(0, weight=1)
# project.grid_columnconfigure(0, weight=1)

# project.mainloop()

import tkinter as tk
import threading
from pytube import YouTube, request
import sys

is_paused = is_cancelled = False


# def progress_function(chunk, file_handle, bytes_remaining):
#     global filesize
#     current = ((filesize - bytes_remaining)/filesize)
#     percent = ('{0:.1f}').format(current*100)
#     progress = int(50*current)
#     status = '█' * progress + '-' * (50 - progress)
#     sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
#     sys.stdout.flush()
# yt_obj = YouTube("https://youtube.com/shorts/rtxxEIW5VX0?feature=share", on_progress_callback = progress_function)

# yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(output_path='C:/vdo from tube', filename='MyVideo')
def download_video(url):
    global is_paused, is_cancelled
    download_button['state'] ='disabled'
    pause_button['state'] ='normal'
    cancel_button['state'] ='normal'
    try:
        progress['text'] = 'Connecting ...'
        yt = YouTube(url)
        stream = yt.streams.first()
        filesize = stream.filesize  # get the video size
        with open('sample.mp4', 'wb') as f:
            is_paused = is_cancelled = False
            # stream.download('C:/vdo from tube/')
            stream = request.stream(stream.url) # get an iterable stream
            downloaded = 0
            while True:
                if is_cancelled:
                    progress['text'] = 'Download cancelled'
                    break
                if is_paused:
                    continue
                chunk = next(stream, None) # get next chunk of video
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    progress['text'] = f'Downloaded {downloaded} / {filesize}'
                    print(f'Downloaded {downloaded} / {filesize}')
                else:
                    # no more data
                    progress['text'] = 'Download completed'
                    break
        print('done')
    except Exception as e:
        print(e)
    download_button['state'] ='normal'
    pause_button['state'] ='disabled'
    cancel_button['state'] ='disabled'

def start_download():
    threading.Thread(target=download_video, args=(url_entry.get(),), daemon=True).start()

def toggle_download():
    global is_paused
    is_paused = not is_paused
    pause_button['text'] = 'Resume' if is_paused else 'Pause'

def cancel_download():
    global is_cancelled
    is_cancelled = True

root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text='URL:').grid(row=0, column=0, sticky='e')
url_entry = tk.Entry(root, width=60)
url_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

download_button = tk.Button(root, text='Download', width=20, command=start_download)
download_button.grid(row=1, column=2, sticky='e', padx=10, pady=(0,10))

pause_button = tk.Button(root, text='Pause', width=10, command=toggle_download, state='disabled')
pause_button.grid(row=2, column=0)

progress = tk.Label(root)
progress.grid(row=2, column=1, sticky='w')

cancel_button = tk.Button(root, text='Cancel', width=10, command=cancel_download, state='disabled')
cancel_button.grid(row=2, column=2, sticky='e')

root.mainloop()

# from pytube import YouTube
# import tkinter as tk
# from tkinter import ttk
# import threading


# # main application shows:
# # label Loading..
# # label which configure values when file is downloading 
# # inderterminate progress bar

# class MainApplication(tk.Frame):

#     def __init__(self, master=None, *args, **kwargs):
#         tk.Frame.__init__(self, master)
#         self.master = master

#         self.master.grid_rowconfigure(0, weight=0)
#         self.master.grid_columnconfigure(0, weight=1)

#         self.youtubeEntry = "https://youtube.com/shorts/nQr3FoJb5x8?feature=share"
#         self.FolderLoacation = "C:/vdo from tube/"

#         # pytube
#         self.yt = YouTube(self.youtubeEntry)

#         video_type = self.yt.streams.filter(only_audio = True).first()

#         # file size of a file
#         self.MaxfileSize = video_type.filesize

#         # Loading label
#         self.loadingLabel = ttk.Label(self.master, text="Loading...", font=("Agency FB", 30))
#         self.loadingLabel.grid(pady=(100,0))

#         # loading precent label which must show % donwloaded
#         self.loadingPercent = tk.Label(self.master, text="0", fg="green", font=("Agency FB", 30))
#         self.loadingPercent.grid(pady=(30,30))

#         # indeterminate progress bar
#         self.progressbar = ttk.Progressbar(self.master, orient="horizontal", length=500, mode='indeterminate')
#         self.progressbar.grid(pady=(50,0))
#         self.progressbar.start()    

#         threading.Thread(target=self.yt.register_on_progress_callback(self.show_progress_bar)).start()

#         # call Download file func
#         threading.Thread(target=self.DownloadFile).start()



#     def DownloadFile(self):


#         self.yt.streams.filter(only_audio=True).first().download(self.FolderLoacation)

#     # func count precent of a file
#     def show_progress_bar(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):

#         # loadingPercent label configure value %
#         self.loadingPercent.config(text=str(int(100 - (100*(bytes_remaining/self.MaxfileSize)))))


# root = tk.Tk() 
# root.title("Youtube downloader")
# root.geometry("1920x1080")
# app = MainApplication(root)
# root.mainloop()