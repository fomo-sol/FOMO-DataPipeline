from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# 크롬 드라이버 경로 설정
driver = webdriver.Chrome()  # or specify driver path

url = "https://www.federalreserve.gov/monetarypolicy/fomcprojtable20220316.htm"
driver.get(url)

# JS 로딩 대기
time.sleep(5)

# 렌더링된 페이지의 HTML 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 원하는 div 추출
target_div = soup.find("div", class_="col-xs-12 col-sm-8 col-md-8")

# 저장
with open("20220316_fomcproj.html", "w", encoding="utf-8") as f:
    f.write(str(target_div))

driver.quit()
