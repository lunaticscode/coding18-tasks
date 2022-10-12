import use_chromdriver as ud
import use_selector as us
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

target_url = "https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do"
driver = ud.make_web_driver()
driver.get(target_url) # 자동화 브라우저에 target_url을 적용해서 가동시킨다.

# 혹시나 팝업창이 생성됬다면 종료하기 위한 코드
try:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
except Exception as err:
    print('팝업 안뜸')

driver.find_element(By.CSS_SELECTOR, us.START_INPUT_SELECTOR).clear()
driver.find_element(By.CSS_SELECTOR, us.START_INPUT_SELECTOR).send_keys("서울")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, us.END_INPUT_SELECTOR).clear()
driver.find_element(By.CSS_SELECTOR, us.END_INPUT_SELECTOR).send_keys("부산")
time.sleep(1)
selected_day_elem = Select(driver.find_element(By.CSS_SELECTOR, us.SELECT_DAY_SELECTOR))
selected_day_elem.select_by_value("27")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, us.SUBMIT_BUTTON_SELECTOR).click()
time.sleep(2)

# 혹시나 팝업창이 생성됬다면 종료하기 위한 코드
try:
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
except Exception as err:
    print('팝업 안뜸')

time.sleep(5)
page_html = BeautifulSoup(driver.page_source, 'html.parser')
time_table_elem = page_html.select_one(us.TIME_TABLE_SELECTOR)
time_table_row_elems = time_table_elem.select("tr")
time_table_row_elems.pop(0)
for row in time_table_row_elems: 
    train_name = row.select_one("td:nth-child(2)").get("title")
    if train_name == "":
        train_name = "새마을호"
    start_time = row.select_one("td:nth-child(3)").text.strip()
    end_time = row.select_one("td:nth-child(4)").text.strip()
    print(f'출발 시간 {start_time} / 도착 시간 {end_time} / {train_name}')

time.sleep(5)
