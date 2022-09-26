from pytube import Playlist
youtube = Playlist("https://www.youtube.com/watch?v=PfUSS0liJ4M&list=PLwGdqUZWnOp3MYf_RHWAm48qvMjap7J7S")
print(len(youtube))

for link in youtube:
    print(link)
for video in youtube.videos:
    name = video.title
    print(name)
    
# import re
 
# # Example input string
# string = "[~How! @are# $you% ^doing& *today\(). _I- +hope=| <everything> `is~ {fine}]"
 
# # Only keep:
# # Letters a-z, A-Z
# # Dots (.)
# # Numbers (\d)
# # Non white space (\s)
# # ^ means other than the provided patterns
# # need to be substituted by an empty string
# string = re.sub('[^a-zA-Z.\d\s]', '', string)
 
# # Print the final string. This should print:
# # How are you doing today. I hope everything is fine
# print(string)