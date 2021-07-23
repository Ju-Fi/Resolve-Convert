# Resolve-Convert

Commonly used codecs like h264 and aac are not supported in the free version of Davinci Resolve on Linux. These are very basic scripts to transcode video files to uncompressed codecs that Resolve supports. 

## Usage
Download these scripts and put them into your directory of choice. 

Create two folders within the same directory as these scripts: `compress` and `uncompress`. 

In order to uncompress the files to use them in Resolve, put them in the `uncompress` folder and run `uncompress.py`. 

To compress the files into more efficient codecs (h264/NVENC and aac), put them into the `compress` folder and run `compress.py`.


## Dependencies
- Python 3.6.8 or later
- FFmpeg (should be installed on Linux distros by default)

## Notes
I am not an expert in FFmpeg, in fact I'm quite new, so if the quality of the output video is decreased in terms of visuals and/or audio, please let me know so I can look into making adjustments. You can contact me via Twitter [@FighterJurassic](https://twitter.com/FighterJurassic) or DM me on Discord **Jurassic#1119*. 

Similarly, if you have a suggestion as to how to improve the quality in FFmpeg, please let me know as well. These scripts are *extremely* basic, and so are very easy to modify if you need to output to a different directory, or change the FFmpeg settings.

