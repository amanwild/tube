from random import randrange
import os
# for single video download
from pytube import YouTube
import random  
import string  


link = "https://www.youtube.com/watch?v=xR3V5Ow2dTI&list=RDXJoFZQqTZ5g&index=3"

youtube = YouTube(link)
Title =youtube.title
print("\n Title : ", Title)

# videos =youtube.streams.filter(only_video=True)#it give all formates
videos = youtube.streams.all()  # it give all formates

vid = list(enumerate(videos))
reslist = []#For Storing All Available resulation
a = 0

print(videos[len(vid)-1])

for i in vid:
    print(i)
    
for i in vid:
    #Geting all metadata form vid
    tupl = list(i)
    strtupl = str(tupl[1])
    metalist = list(strtupl.split())

    tyvi = 'type="video">'
    if (metalist[-1] == tyvi):
        res = ''.join(filter(lambda i: i.isdigit(), metalist[3]))
        reslist.append(int(res))
        
print(reslist, " After append")
# maxx = reslist.index(max( int(i) for i in reslist))

#max resulation
max_value = max(reslist)
#index of max resulation
max_indes = reslist.index(max_value)
print(max_indes, " index ", max(reslist), "max index res")

indices = [index for index, value in enumerate(reslist) if value == max_value]

print(indices, "max indices")
print(max(indices), "max indices")
maxx = max(indices)

code = ''.join((random.choice(string.ascii_lowercase) for x in range(3))) # run loop until the define length
print(code)

videos[(len(vid)-1)].download(r"D:/vdo from tube")

os.rename(r"D:/vdo from tube/"+videos[len(vid)-1].default_filename, r"D:/vdo from tube/"+str(code)+" "+videos[len(vid)-1].default_filename)

# videos[maxx].download("C:/videos")
# os.rename(videos[maxx].default_filename, str(code)+youtube.title.default_filename)

print("Successfully Download")
##################################################################################
# strm= int(input("enter: "))

# # yt = YouTube("https://www.youtube.com/watch?v=phWncNF1LpQ&list=RDphWncNF1LpQ&start_radio=1")
# # yt = yt.get('mp4', '720p')
# # yt.download('D:\vscode\.vscode\youtube video downloader')
##################################################################################

# from pytube import YouTube
# YouTube('https://www.youtube.com/watch?v=phWncNF1LpQ&list=RDphWncNF1LpQ&start_radio=1').streams.first().download('D:\\vscode\\.vscode\\youtube video downloader')
##################################################################################

# #best Quality video
# from pytube import YouTube
# import os

# def downloadYouTube(videourl, path):

#     yt = YouTube(videourl)
#     yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#     if not os.path.exists(path):
#         os.makedirs(path)
#     yt.download(path)

# downloadYouTube('https://www.youtube.com/watch?v=BddP6PYo2gs', 'D:/vscode/.vscode/youtube video downloader')
##################################################################################
# import pytube
# link = "https://www.youtube.com/watch?v=BddP6PYo2gs"
# yt = pytube.YouTube(link)
# print("Title:", yt.title)
# print("Author:", yt.author)
# print("Number of views:", yt.views)
# print("Length of video:", yt.length, "seconds")
# yt.streams.get_highest_resolution().download()
# print("Video successfullly downloaded from", link)
##################################################################################
# #for playlist

# from pytube import Playlist
# p = Playlist('https://www.youtube.com/watch?v=LXb3EKWsInQ&t=249s')

# print(f'Downloading: {p.title}')

# for video in p.videos:
#     video.streams.first().download()
##################################################################################

# ##for channel
# from pytube import Channel
# c = Channel('https://www.youtube.com/c/ProgrammingKnowledge')

# print(f'Downloading videos by: {c.channel_name}')

# for video in c.videos:
#     video.streams.first().download()


##################################################################################
