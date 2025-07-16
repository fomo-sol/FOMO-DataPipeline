import os
from bs4 import BeautifulSoup

# 디렉토리 경로 설정
input_dir = './FOMC_Meeting_Statement/원문html'
output_dir = './FOMC_Meeting_Statement/원문txt'
os.makedirs(output_dir, exist_ok=True)

# HTML → TEXT 추출 함수
def extract_text_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    # 텍스트만 추출 후 줄바꿈/공백 정리
    text = soup.get_text(separator='\n')
    cleaned = '\n'.join([line.strip() for line in text.splitlines() if line.strip()])
    return cleaned

# 전체 파일 반복 처리
for filename in os.listdir(input_dir):
    if filename.endswith('_statement_en.html'):
        html_path = os.path.join(input_dir, filename)
        text_content = extract_text_from_html(html_path)

        # .txt 파일로 저장
        base_name = filename.replace('.html', '.txt')
        txt_path = os.path.join(output_dir, base_name)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(text_content)

        print(f"✅ 저장 완료: {base_name}")
