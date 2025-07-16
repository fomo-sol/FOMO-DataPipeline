import json

# 기존 FOMC.json을 로드
with open('FOMC.json', 'r') as f:
    fomc_data = json.load(f)

fomo_full_data = {}

for year, entries in fomc_data.items():
    fomo_full_data[year] = []

    for entry in entries:
        date = entry["date"]  # ex: 2025-01-29
        yyyymmdd = date.replace("-", "")  # ex: 20250129

        # 각 필드별 URL 구성
        base_url = "https://www.federalreserve.gov"
        item = {
            "date": date,
            "press_conference": f"{base_url}/monetarypolicy/fomcpresconf{yyyymmdd}.htm",
            "statement": f"{base_url}/newsevents/pressreleases/monetary{yyyymmdd}a.htm",
            "implementation_note": f"{base_url}/newsevents/pressreleases/monetary{yyyymmdd}a1.htm",
            "projection_materials": f"{base_url}/monetarypolicy/fomcprojtabl{yyyymmdd}.htm",
            "press_conference_pdf": f"{base_url}/mediacenter/files/FOMCpresconf{yyyymmdd}.pdf",
            "minutes": f"{base_url}/monetarypolicy/fomcminutes{yyyymmdd}.htm"
        }

        fomo_full_data[year].append(item)

# 결과 저장
with open('FOMO_full.json', 'w') as f:
    json.dump(fomo_full_data, f, indent=2)
