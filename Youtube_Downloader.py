from pytube import YouTube

try:
    # Ask the user to input the YouTube URL.
    url = input("Enter the YouTube URL:")

    you_video = YouTube(url)

    # Display the title of the YouTube Video.
    print("Title: ", you_video.title)

    # Display the current view of the YouTube Video.
    print("View: ", you_video.views)

    # Download the highest quality of the video.
    you_download = you_video.streams.get_highest_resolution()

    # Save the file to certain folder.
    you_download.download("/workspace/projects/Video_Downloader/Video_Downloaded")

    print("Download Complete.")

# Raise error when the download failed.
except Exception as e:
    print("An error occured", str(e))
