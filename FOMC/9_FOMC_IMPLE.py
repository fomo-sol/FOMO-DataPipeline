import os
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# FOMO_full.json 로드
with open('FOMO_full.json', 'r', encoding='utf-8') as f:
    fomc_data = json.load(f)

output_dir = 'FOMC_Implementation_Note'
os.makedirs(output_dir, exist_ok=True)

def save_third_row_html(url, date_str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # 세 번째 .row 찾기
        rows = soup.select('div#content div.row')
        if len(rows) < 3:
            print(f"[{date_str}] ❌ row가 충분하지 않음")
            return

        third_row = rows[2]  # 인덱스는 0부터 시작
        html = third_row.prettify()

        filename = f"{date_str}_implementation_en.html"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[{date_str}] ✅ 저장 완료")
    
    except Exception as e:
        print(f"[{date_str}] ⚠️ 에러: {e}")

# 전체 반복
for year, events in fomc_data.items():
    for event in tqdm(events, desc=f"{year} 처리 중"):
        date = event["date"]
        url = event.get("implementation_note")
        if url:
            save_third_row_html(url, date)
