from pytube import Playlist
from moviepy.editor import *
import os.path
import re
from os.path import exists
from random import randrange
from playsound import playsound
from pytube import extract
from pathlib import Path
import os
from pathlib import Path, PureWindowsPath
# import subprocess
import threading
from threading import Thread
import ffmpeg
import moviepy.editor as mpe
from pytube import YouTube
link = "https://youtu.be/HXDD7-EnGBY"
try:
    youtube = Playlist(link)
    print(f'Playlist: {youtube.title}')
  
    vid = list(enumerate(youtube.videos))
    print("WELCOME to TUBE", vid in youtube.videos)
    for vid in youtube.videos:
        print(vid,"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
     
except :
  id=extract.video_id(link)
  print(id)
  pass
try:
    print(0)
except print(0):
    pass