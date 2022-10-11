import requests
from bs4 import BeautifulSoup

target_url = "https://www.daangn.com/kr/realty/"
response = requests.get(target_url)
soup = BeautifulSoup(response.text, "html.parser")

article_list = soup.select("div._11vv8ke2")
for job in article_list:
    title = job.select_one("div.w7pzr91").text
    location = job.select_one("div.w7pzr92").text
    price = job.select_one("div.w7pzr93").text
    print(f'[제목] {title}\n[위치] {location}\n[가격] {price}\n\n')