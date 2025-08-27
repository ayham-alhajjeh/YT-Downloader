"""
YouTube Video Downloader
Author: Ayham Alhajjeh
Created: 2025-08-27
Description: Simple Python script to download YouTube videos using pytube.
"""

from pytubefix import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)





