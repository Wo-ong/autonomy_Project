from selenium import webdriver
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from urllib.request import urlopen
from multiprocessing import Pool

path = 'C:/Users/wjsdn/Desktop/chromedriver_win32/chromedriver.exe'

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

browser = webdriver.Chrome(path, options=options)

browser.maximize_window()

keywords = ['하지루틴 스트레칭1','윗몸 말아올리기','걷기']

def find_link():

    for words in keywords:
        url = "https://www.youtube.com/channel/UCQL8LeERxJ4HiS0I3T-8qGA/search?query=" + words

        browser.get(url)
        time.sleep(1)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        attr = soup.find("div", id="dismissible").find("a")["href"]

        link = "https://www.youtube.com/embed/" + attr[9:]

        print("-----------------가져온 내용-----------------")
        print(link)

if __name__=='__main__':
    pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
    pool.map(find_link())

