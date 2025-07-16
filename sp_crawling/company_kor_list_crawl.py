import requests
from bs4 import BeautifulSoup
import json
url = "https://www.hankyung.com/globalmarket/usa-stock-sp500"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

results = []
rows = soup.select("tbody tr")

for row in rows:
    name_div = row.select_one("div.stock-name")
    symbol_div = row.select_one("div.symbol.txt-en")
    
    if name_div and symbol_div:
        name = name_div.text.strip()
        symbol = symbol_div.text.strip()
        results.append({
            "company_kor": name,
            "symbol": symbol
        })

output_path = "sp500_list_kor.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"{len(results)}개 종목{output_path}에 저장.")
