import os
import json
import requests

# === 경로 설정 ===
json_path = "./FOMO_full.json"
save_dir = "./FOMC_Conference_Transcript"
os.makedirs(save_dir, exist_ok=True)

# === JSON 파일 로드 ===
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# === PDF 다운로드 함수 ===
def download_pdf(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"저장 완료: {save_path}")
        else:
            print(f"다운로드 실패 (HTTP {response.status_code}): {url}")
    except Exception as e:
        print(f"예외 발생: {e} - {url}")

# === 연도별 순회 ===
for year, meetings in data.items():
    for meeting in meetings:
        date = meeting.get("date")  # 예: 2025-01-29
        pdf_url = meeting.get("press_conference_pdf")

        if not pdf_url:
            continue  # 해당 회의에 PDF 없음

        filename = f"{date.replace('-', '')}_transcript_en.pdf"
        save_path = os.path.join(save_dir, filename)

        print(f"다운로드 중: {date} - {pdf_url}")
        download_pdf(pdf_url, save_path)

print("\n 모든 PDF 다운로드 완료!")
