import deepl
from bs4 import BeautifulSoup

# 1. Deepl API Key
DEEPL_API_KEY = "a98549a1-f7e3-477e-8463-91b73a0d8497:fx"  # ← 여기에 본인 키 입력

# 2. 파일 읽기
with open("20250618_fomcproj_en.html", "r", encoding="utf-8") as f:
    html = f.read()

# 3. HTML에서 본문 텍스트 추출
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text(separator="\n", strip=True)

# 4. Deepl 번역
translator = deepl.Translator(DEEPL_API_KEY)
translated = translator.translate_text(text, source_lang="EN", target_lang="KO")

# 5. 저장
with open("20250618_fomcproj_ko.txt", "w", encoding="utf-8") as f:
    f.write(translated.text)

print("번역 완료: 20250618_fomcproj_ko.txt")
