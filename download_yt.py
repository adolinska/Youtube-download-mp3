from pytube import YouTube
from moviepy.editor import *
import os

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

directory = "C:\\Users\\amela\\Desktop\\Projects\\RVC\\test_audio"

names = []
while True:
    link = input('Insert link: (press q to exit) ')
    
    if link == 'q':
        break
    else:
        names.append(link)

for name in names:
    try: 
        t = YouTube(name).streams.filter(resolution='720p')
        t[0].download(directory)
    except Exception as e:
        print("Error occured:", e)

mp4_names = [file for file in os.listdir(directory) if file.endswith(".mp4")]

# for name in mp4_names:
#     MP4ToMP3(os.path.join(directory, name), os.path.join(directory, name[:-4] + '.mp3'))
#     os.remove(os.path.join(directory, name))

print('Done')


