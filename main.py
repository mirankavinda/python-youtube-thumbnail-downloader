# Import the pytube and urllib libraries
from pytube import YouTube
import urllib.request

# Enter the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object and get the thumbnail URL
yt = YouTube(url)
thumbnail_url = yt.thumbnail_url

# Download the thumbnail image and save it as thumbnail.jpg
urllib.request.urlretrieve(thumbnail_url, "thumbnail.jpg")

# Print a success message
print("Thumbnail downloaded successfully!")
