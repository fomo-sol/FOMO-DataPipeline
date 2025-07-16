import os
from bs4 import BeautifulSoup

input_dir = 'FOMC_Meeting_Minutes/원문html'
output_dir = 'FOMC_Meeting_Minutes/원문txt'
os.makedirs(output_dir, exist_ok=True)

def extract_text_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # 텍스트 추출 후 정리
    text = soup.get_text(separator='\n')
    cleaned = '\n'.join([line.strip() for line in text.splitlines() if line.strip()])
    return cleaned

for filename in os.listdir(input_dir):
    if filename.endswith('_minutes_en.html'):
        html_path = os.path.join(input_dir, filename)
        text_content = extract_text_from_html(html_path)

        # 저장할 텍스트 파일 경로
        base_name = filename.replace('.html', '.txt')
        txt_path = os.path.join(output_dir, base_name)

        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text_content)

        print(f"✅ 저장 완료: {base_name}")
