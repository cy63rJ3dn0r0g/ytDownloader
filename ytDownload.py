import yt_dlp
import os

url = input('Enter YouTube URL: ')
artistName = input('Enter the desired singer name: ')
songName = input('Enter the desired song name: ')
extention = input('Enter the desired extension: ')

filename= artistName.capitalize() + ' - ' + songName.capitalize() + '.' + extention
if os.path.exists(filename):
    print("The file '{filename}' already exists.")
else:
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

