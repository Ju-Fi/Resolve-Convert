import os

UncompressDir = "./uncompress/"

for i in os.listdir(UncompressDir):
    if i.endswith(".mp4"):
        i = i.replace(' ', '\ ')
        os.system(f"ffmpeg -i {UncompressDir}{i} -c:v mpeg4 -q:v 0 -c:a pcm_s16le {i}.uncompressed.mov")
