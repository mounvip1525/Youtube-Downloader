from pytube import YouTube

# yt=YouTube("https://www.youtube.com/watch?v=TH3d5cyeer0")

# # print(yt.streams.all())
# # print(yt.streams.get_by_itag(22))

# dw=yt.streams.get_by_itag(22)
# dw.download("D:/")

# video_links=['https://www.youtube.com/watch?v=TH3d5cyeer0','https://www.youtube.com/watch?v=wtQ_tBSrgVM']
video_links=open("videolinks.txt","r")
for i in video_links:
    yt=YouTube(i)
    try:
        dw=yt.streams.get_by_itag(22)
        #dw=yt.streams.first()
        dw.download("D:/")
        print("Video successfully downloaded")
    except:
        print("Download failed ",i)