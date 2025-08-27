"""
YouTube Video Downloader
Author: Ayham Alhajjeh
Created: 2025-08-27
Description: Simple Python script to download YouTube videos using pytube.
"""

from pytubefix import YouTube
from sys import argv
import sys

def progress_func(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = int(bytes_downloaded / total_size * 100)
    bar = "=" * (percent // 2) + "-" * (50 - percent // 2)
    sys.stdout.write(f"\r[{bar}] {percent}%")
    sys.stdout.flush()

def complete_func(stream, file_path):
    print(f"\nDownload Complete: {file_path}")



link = argv[1]
yt = YouTube(link, on_progress_callback=progress_func, on_complete_callback=complete_func)

print("Title: ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download()