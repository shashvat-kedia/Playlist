import time
import subprocess
import youtube_dl

url_list = []
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
while True:
    print("1.To enter link to new song")
    print("2. Exit")
    choice = int(input())
    if choice==1:
        url = input()
        url_list.append(url)
    elif choice==2:
        break
for urls in url_list:
    url = urls
    with ydl:
        result = ydl.extract_info(
            url,download=False)
    if 'entries' in result:
        video = result['entries'][0]
    else:
        video = result
    print(video.duration)
    p = subprocess.Popen("opera",url)
    time.sleep(video.duration+10)
    p.kill()

    
    
