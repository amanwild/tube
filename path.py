from pytube import Playlist
youtube = Playlist("https://www.youtube.com/watch?v=PfUSS0liJ4M&list=PLwGdqUZWnOp3MYf_RHWAm48qvMjap7J7S")
print(len(youtube))

for link in youtube:
    print(link)
for video in youtube.videos:
    name = video.title
    print(name)