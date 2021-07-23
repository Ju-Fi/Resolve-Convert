import os

CompressDir = "./compress/"

nvenc = input("Use NVENC (Nvidia GPU)? y/n: ").lower()

for i in os.listdir(CompressDir):
    if nvenc == "y":
        if i.endswith(".mov"):
            i = i.replace(' ', '\ ')
            os.system(f"ffmpeg -i {CompressDir}{i} -c:v h264_nvenc -crf 22 -c:a aac {i}.compressed.mp4")
    if nvenc == "n":
        if i.endswith(".mov"):
            i = i.replace(' ', '\ ')
            os.system(f"ffmpeg -i {CompressDir}{i} -c:v libx264 -crf 22 -c:a aac {i}.compressed.mp4")

