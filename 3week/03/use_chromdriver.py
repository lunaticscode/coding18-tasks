from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

def make_web_driver(): # selenium 전용 자동화 Chrome 설정
    path = chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options, service=Service(path))
    driver.implicitly_wait(10)
    return driver