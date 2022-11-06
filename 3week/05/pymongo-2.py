import requests
from bs4 import BeautifulSoup
from db_init import db

target_url = "https://www.daangn.com/kr/realty/"
response = requests.get(target_url)
soup = BeautifulSoup(response.text, "html.parser")


# ============ 1) 당근마켓 부동산 정보 DB에 저장 ============= #

def insert_info(info): 
    try:
        db['dummy_realty'].insert_one(info)
    except ValueError as err:
        print(f'(!)DB Error {err}')
        return False
    return True    

def scraping_realty():
    article_list = soup.select("div._11vv8ke2")
    for job in article_list:
        title = job.select_one("div.w7pzr93").text
        location = job.select_one("div.w7pzr94").text
        price = job.select_one("div.w7pzr95").text
        # print(f'[제목] {title}\n[위치] {location}\n[가격] {price}\n\n')
        
        realty_info = {
            "title": title,
            "location": location,
            "price": price,
        }
        insert_info(realty_info)

# 아래 주석을 풀어주세요
# scraping_realty()
# =========================================================== #



# ============ 2) price에 "월세" 가 들어간 부동산 정보 가져오기 ============= #

def get_monthly_price_realtys():
    try:
        info_list = db['dummy_realty'].find({"price": { "$regex" : "^월세"}})
        return list(info_list)
    except ValueError as err:
        print(f'(!)DB Error {err}') 
        return False

# 아래 주석을 풀어주세요
# result_list = get_monthly_price_realtys()
# for info in result_list:
#     print(info)
# =================================================================== #