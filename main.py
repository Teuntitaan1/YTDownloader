import pytube.exceptions
from pytube import YouTube
from pathlib import Path
import os

# Gets the url object
Video = None
while 1:
    VideoInput = input("Url to the video you want to download?")
    try:
        Video = YouTube(VideoInput)
        ValidateURL = Video.streams

        # Only breaks when the url is valid
        break

    except pytube.exceptions.VideoUnavailable:
        print("ERROR: Url is not valid, please try another Url")


AudioOnly = False
while 1:
    AudioOnlyInput = input("Do you want to only download the audio? Y/N")
    if AudioOnlyInput == "Y":
        AudioOnly = True
        break
    elif AudioOnlyInput == "N":
        AudioOnly = False
        break

# Gets the available streams to downlaod based on the chosen options
if not AudioOnly:
    AvailableStreams = Video.streams.filter(type="video", mime_type="video/mp4")
else:
    AvailableStreams = Video.streams.filter(type="audio", mime_type="audio/mp4")

index = 0
# Stream choice
for stream in AvailableStreams:
    print(f"[{index}] {stream}")
    index += 1
# Selects the stream to download
StreamToDownload = AvailableStreams[int(0)]
while 1:
    StreamToDownloadInput = input("Select the index of the stream you want to download.")
    # noinspection PyBroadException
    try:
        ValidateStream = AvailableStreams[int(StreamToDownloadInput)]
        StreamToDownload = AvailableStreams[int(StreamToDownloadInput)]
        break

    except:
        print("ERROR: Invalid index, please try another index.")

# Selects where to and downloads the stream.
while 1:
    print("[0] Current directory \n[1] Download directory")

    DownloadLocationInput = input("Select the index of the stream you want to download.")
    if DownloadLocationInput == "0":
        print(f"Downloading Stream {int(StreamToDownloadInput)} ...")
        StreamToDownload.download()
        break
    elif DownloadLocationInput == "1":
        print(f"Downloading Stream {int(StreamToDownloadInput)} ...")
        StreamToDownload.download(output_path=str(os.path.join(Path.home(), "Downloads")))
        break

while 1:
    print("Download completed. Press CTRL + C to exit the program.")
    input("")
