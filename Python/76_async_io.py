# Async IO in Python

# This code demonstrates the use of asynchronous I/O in Python.
# It uses the asyncio library to create tasks for downloading images from a list of URLs.
# The download_image function is an asynchronous function that takes a URL and a filename as input.
# It uses the requests library to make a GET request to the URL and writes the response content to the specified filename.
# The main function creates a list of URLs and filenames, and then creates a task for each image download.
# It uses the asyncio.gather function to wait for all tasks to complete.

import asyncio 
import requests


async def download_image(url, filename):
  print(f"Downloading {filename} from {url}") 
  response = requests.get(url)
  open(filename, "wb").write(response.content)
  print(f"Downloaded {filename} from {url}")

async def main():
  # Define the URLs and filenames
  urls = [
    "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg",
    "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg",
    "https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
  ]
  filenames = ["img1.png", "img2.png", "img3.png"]

  # Create tasks for each image download
  tasks = [download_image(url, filename) for url, filename in zip(urls, filenames)]

  # Wait for all tasks to complete
  await asyncio.gather(*tasks)

asyncio.run(main())
