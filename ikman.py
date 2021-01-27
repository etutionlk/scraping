#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import json

url = requests.get("https://ikman.lk/en/ads/kalutara")


def check_url_status(context=None, event=None):
    if url.status_code == 200:
        soup = BeautifulSoup(url.content, "html.parser")
        all_adds = soup.find_all("li", class_="gtm-normal-ad")
        add_data = []
        for single_ad in all_adds:
            add_data.append(
                {
                    "add_link": "https:/" + single_ad.find("a")["href"],
                    "ad_title": single_ad.find("h2").text,
                    "ad_description": single_ad.find(
                        "div", class_="description--2-ez3"
                    ).text,
                    "ad_price": single_ad.find("span").text,
                }
            )

        return json.dumps(
            {
                "status": url.status_code,
                "message": "Advertisment URL is working properly",
                "data": json.dumps(add_data),
            }
        )
    else:
        return {"status": url.status_code, "message": "Not Working Properly."}


print(check_url_status())