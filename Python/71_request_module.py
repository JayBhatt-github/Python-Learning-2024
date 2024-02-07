# Request Module in Python

import requests  # Importing the requests library
from bs4 import BeautifulSoup  # Importing the BeautifulSoup library

url = "https://www.python.org"  # Assigning the URL to a variable
r = requests.get(url)  # Sending a GET request to the URL and storing the response in a variable

soup = BeautifulSoup(r.text, 'html.parser')  # Creating a BeautifulSoup object to parse the HTML content of the response
for heading in soup.find_all("title"):  # Finding all the title tags in the HTML content
  print(heading.text)  # Printing the text inside each title tag
