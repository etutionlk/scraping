#!/usr/bin/python

# bbImageWrapper

import requests
from bs4 import BeautifulSoup
import time


page = requests.get(
    "https://elakiri.com/threads/licentiou-ouls-non_nude.1966460/page-6"
)

soup = BeautifulSoup(page.content, "html.parser")

# https://elakiri.com/threads/toyota-noah-557000km-story.1971725/

divs = soup.find_all("div", class_="bbImageWrapper")

count = 1

for div in divs:
    img_element = div.find("img")
    img_url = "http://" + img_element["src"].strip("/")

    img_data = requests.get(img_url).content
    with open("image_name" + str(int(time.time())) + ".jpg", "wb") as handler:
        handler.write(img_data)

    count += 1
