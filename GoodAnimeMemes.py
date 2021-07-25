'''
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
  ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄
ZUMBY NSR CC [...]
'''

import requests
from bs4 import BeautifulSoup
import time


headers = {'User-Agent': 'xxxxxxxxxxxxxxxxxxxx'}

url = "https://www.reddit.com/r/Animemes/"


r = requests.get(url, headers=headers)
# Check connection to website
if r.status_code == 200:
  print("Connected to website!")
  time.sleep(0.5)
elif r.status_code == 400:
  print("Page does not exist...")
  time.sleep(0.5)
elif r.status_code == 500:
  print("Unauthorized access!")
  time.sleep(0.5)
else:
  pass


soup = BeautifulSoup(r.text, 'html.parser')
# Print Title of Website
print(soup.title.text)
time.sleep(0.5)


links = soup.find_all("img", {"alt": "Post image"})
# Print How Many Links There Are
print("There are", len(links), "links to work with.")
time.sleep(0.8)


images = []
for link in links:
  if link.has_attr('src'):
    # append individual URL to "images" list
    images.append(link['src'])

# Set initial n value
n = 0

# Loop through list of URLs and download each with name "anime" + n
for image in images:
  n = n + 1
  with open ("anime" + str(n) + '.jpg', 'wb') as f:
    im = requests.get(image)
    f.write(im.content)
