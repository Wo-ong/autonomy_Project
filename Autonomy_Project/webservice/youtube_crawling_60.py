from selenium import webdriver
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool

path = 'C:/Users/jeonghun7898/Downloads/chromedriver_win32/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("headless")

browser = webdriver.Chrome(path, options=options)
browser.maximize_window()

from read_sql_60 import pre_result, main_result, last_result
keywords = [pre_result[0], main_result[0], last_result[0]]

def find_link():
    links = []
    for words in keywords:
        url = "https://www.youtube.com/channel/UCQL8LeERxJ4HiS0I3T-8qGA/search?query=" + words

        browser.get(url)
        time.sleep(1)

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        attr = soup.find("div", id="dismissible").find("a")["href"]

        link = "https://www.youtube.com/embed/" + attr[9:]

        links.append(link)

    return links

if __name__=='__main__':
    pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
    pool.map(find_link())




