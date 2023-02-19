# AIzaSyBIM0Qg7QVTDqqBn6vtaxol_k9ffpFWfQw API youtube data API v3
from googleapiclient.discovery import build
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

link = "https://youtube.com/shorts/ByVonzqiF20?feature=share"
try:
    youtube = Playlist(link)
    print(f'Playlist: {youtube.title}')
  
    vid = list(enumerate(youtube.videos))
    print("WELCOME to TUBE", vid in youtube.videos)
    for vid in youtube.videos:
        print(vid,"::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
     
except :
  video_id=extract.video_id(link)
  print(video_id)
  pass


api_key = 'AIzaSyBIM0Qg7QVTDqqBn6vtaxol_k9ffpFWfQw'

# recursive function to get all replies in a comment thread
def get_replies(comment_id, token):
    replies_response = yt_object.comments().list(part = 'snippet', maxResults = 100, parentId = comment_id, pageToken = token).execute()

    for reply in replies_response['items']:
        all_comments.append(reply['snippet']['textDisplay'])

    if replies_response.get("nextPageToken"):
        return get_replies(comment_id, replies_response['nextPageToken'])
    else:
        return []


# recursive function to get all comments
def get_comments(youtube, video_id, next_view_token):
    global all_comments

    # check for token
    if len(next_view_token.strip()) == 0:
        all_comments = []

    if next_view_token == '':
        # get the initial response
        comment_list = youtube.commentThreads().list(part = 'snippet', maxResults = 100, videoId = video_id, order = 'relevance').execute()
    else:
        # get the next page response
        comment_list = youtube.commentThreads().list(part = 'snippet', maxResults = 100, videoId = video_id, order='relevance', pageToken=next_view_token).execute()
    # loop through all top level comments
    for comment in comment_list['items']:
        # add comment to list
        all_comments.append([comment['snippet']['topLevelComment']['snippet']['textDisplay']])
        # get number of replies
        reply_count = comment['snippet']['totalReplyCount']
        all_replies = []
        # if replies greater than 0
        if reply_count > 0:
            # get first 100 replies
            replies_list = youtube.comments().list(part='snippet', maxResults=100, parentId=comment['id']).execute()
            for reply in replies_list['items']:
                # add reply to list
                all_replies.append(reply['snippet']['textDisplay'])

            # check for more replies
            while "nextPageToken" in replies_list:
                token_reply = replies_list['nextPageToken']
                # get next set of 100 replies
                replies_list = youtube.comments().list(part = 'snippet', maxResults = 100, parentId = comment['id'], pageToken = token_reply).execute()
                for reply in replies_list['items']:
                    # add reply to list
                    all_replies.append(reply['snippet']['textDisplay'])

        # add all replies to the comment
        all_comments[-1].append(all_replies)

    if "nextPageToken" in comment_list:
        return get_comments(youtube, video_id, comment_list['nextPageToken'])
    else:
        return []


all_comments = []

# build a youtube object using our api key
yt_object = build('youtube', 'v3', developerKey=api_key)

# get all comments and replies
comments = get_comments(yt_object, video_id, '')
i= 1
for comment, replies in all_comments:
    print("("+str(i)+")  "+comment)
    if len(replies) > 0:
        print("There are", len(replies), "replies")
        print("\tReplies:")
        for reply in replies:
            i = i+1
            print("\t"+"("+str(i)+")  " + reply)
    i = i+1
    print()