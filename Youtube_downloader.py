import yt_dlp
import tkinter as tk
from tkinter import filedialog
import time


def download_video(url, save_path):
    """Download a video from YouTube with a fixed quality and retry logic."""

    try_number = 0

    def hook(d):
        if d['status'] == 'finished':
            print('Video downloaded successfully.')
            end_time = time.time()
            elapsed_time = end_time - start_time
            mins, secs = divmod(elapsed_time, 60)
            timer = "{:02d}:{:02d}".format(int(mins), int(secs))
            print(f'Total time elapsed: {timer}')
        elif d['status'] == 'downloading':
            print(f'Downloading... {d["_percent_str"]} ETA: {d["_eta_str"]}')

    while try_number < 5:
        try_number += 1
        try:
            failed_time = time.time()
            print(f'{try_number}th try:')

            # Set YouTube-DL options with fixed format code for 720p
            ydl_opts = {
                'format': '22',  # Format code for 720p
                'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                'progress_hooks': [hook],
            }

            # Download the video using YouTube-DL
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            break  # Break out of the loop if download is successful
        except Exception as e:
            end_time = time.time()
            elapsed_time = end_time - failed_time
            mins, secs = divmod(elapsed_time, 60)
            timer = "{:02d}:{:02d}".format(int(mins), int(secs))
            print(e)
            print(f'Try duration: {timer}')
            if try_number < 5:
                print('Retrying...')
                time.sleep(3)  # Sleep for 3 seconds before the next retry
            else:
                print('Maximum retries reached. Download failed.')


def open_file_dialog():
    """Open a file dialog for selecting a save folder."""
    folder = filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')
    return folder


# Initialize the try_number variable
try_number = 0
# Greetings
print("""Welcome to the YouTube Video Downloader!
Download your favorite videos hassle-free.
Just provide the YouTube video URL, and let's get started!
Note: All videos will be downloaded in 720p resolution.""")
# The main loop
while True:
    # Create and hide the Tkinter root window
    root = tk.Tk()
    root.withdraw()

    # Get YouTube video URL from user input
    url = input('Please enter a YouTube video URL: ')

    save_path = None
    while not save_path:
        print('Please select a folder.')
        # Open a file dialog to select a save folder
        save_path = open_file_dialog()
        if not save_path:
            continue

    print('Download has started.')
    global start_time
    start_time = time.time()

    # Download video with fixed quality (720p)
    download_video(url, save_path)

    # Getting user input before exit
    while True:
        ask_continue = input(
            'Do you want to download another video (Yes/No)? ').lower()
        if ask_continue == 'yes':
            break
        elif ask_continue == 'no':
            break
        else:
            print('Please print "Yes" or "No".')
    # if the answer is "no", breaks the main loop and end.
    if ask_continue == 'no':
        break
