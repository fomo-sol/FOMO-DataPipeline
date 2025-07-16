import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# 폴더 및 JSON 파일 경로
folder_path = "./FOMC_Projection_Materials"
json_path = "./FOMO_full.json"
# Chrome WebDriver 설정
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 안 띄우기
driver = webdriver.Chrome(options=options)

# JSON 로드
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 연도 순회
for year, meetings in data.items():
    for meeting in meetings:
        date = meeting.get("date")
        proj_url = meeting.get("projection_materials")
        
        if not proj_url:
            continue  # projection_materials 없는 경우 skip

        # print(f"처리 중: {date} -> {proj_url}")
        try:
            driver.get(proj_url)
            time.sleep(5)  # JS 로딩 대기

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            target_div = soup.find("div", class_="col-xs-12 col-sm-8 col-md-8")

            if target_div:
                save_path = os.path.join(folder_path, f"{date.replace('-', '')}_fomcproj_en.html")
                with open(save_path, "w", encoding="utf-8") as out:
                    out.write(str(target_div))
                print(f"저장 완료: {save_path}")
            else:
                print(f"✘ div를 찾을 수 없음: {proj_url}")

        except Exception as e:
            print(f"오류 발생: {e} ({proj_url})")

driver.quit()
print("모든 작업 완료.")
