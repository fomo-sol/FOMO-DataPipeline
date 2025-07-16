import requests
from bs4 import BeautifulSoup

# 대상 URL
url = "https://www.federalreserve.gov/newsevents/pressreleases/monetary20250618a.htm"

# HTML 가져오기
response = requests.get(url)
response.raise_for_status()

# 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 해당 div 추출
target_div = soup.find("div", class_="col-xs-12 col-sm-8 col-md-8")

# 저장 (HTML 형식)
with open("20250618_statement.html", "w", encoding="utf-8") as f:
    f.write(str(target_div))

print("저장 완료: 20250618_statement.html")
