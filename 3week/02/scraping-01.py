import requests
from bs4 import BeautifulSoup

target_url = "https://www.daangn.com/kr/realty/"
response = requests.get(target_url) # 위 url로 열리는 페이지의 소스를 가져온다.
soup = BeautifulSoup(response.text, "html.parser") # BeautifulSoup 이 html 방식으로 해석가능하도록 소스를 담아준다.

article_list = soup.select("div._11vv8ke2") # <div class='._11vv8ke2' ... > 인 태그들을 전부 가져온다.
for job in article_list: # 가져온 <<div class='._11vv8ke2'>의 개수만큼 반복문 실행.
    title = job.select_one("div.w7pzr91").text
    location = job.select_one("div.w7pzr92").text
    price = job.select_one("div.w7pzr93").text
    print(f'[제목] {title}\n[위치] {location}\n[가격] {price}\n\n')