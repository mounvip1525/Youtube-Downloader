from pytube import YouTube

yt=YouTube("https://www.youtube.com/watch?v=TH3d5cyeer0")

# print(yt.streams.all())
# print(yt.streams.get_by_itag(22))

dw=yt.streams.get_by_itag(22)
dw.download("D:/")
