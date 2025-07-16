import os
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# 1. 폴더 설정
output_dir = 'FOMC_Meeting_Statement'
os.makedirs(output_dir, exist_ok=True)

# 2. JSON 로드
with open('FOMO_full.json', 'r', encoding='utf-8') as f:
    fomc_data = json.load(f)

# 3. 크롤링 함수
def save_second_row_html(url, date_str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # div#content 내부의 .row 요소 찾기
        content_div = soup.find('div', id='content')
        rows = content_div.select('.row') if content_div else []

        if len(rows) < 2:
            print(f"[{date_str}] ❌ .row insufficient")
            return

        second_row = rows[1]
        html = second_row.prettify()

        filename = f"{date_str}_statement_en.html"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[{date_str}] ✅ 저장 완료")

    except Exception as e:
        print(f"[{date_str}] ⚠️ 에러: {e}")

# 4. 전체 순회
for year, events in fomc_data.items():
    for event in tqdm(events, desc=f"{year} 처리 중"):
        date = event["date"]
        url = event.get("statement")
        if url:
            save_second_row_html(url, date)
