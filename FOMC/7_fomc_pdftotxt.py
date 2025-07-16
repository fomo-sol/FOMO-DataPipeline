import os
import fitz  # PyMuPDF

# PDF 폴더 및 TXT 저장 폴더 경로
pdf_dir = "./FOMC_Conference_Transcript"
txt_dir = os.path.join(pdf_dir, "txt")
os.makedirs(txt_dir, exist_ok=True)

# PDF 파일들 순회
for filename in os.listdir(pdf_dir):
    if filename.endswith("_transcript_en.pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        txt_filename = filename.replace(".pdf", ".txt")
        txt_path = os.path.join(txt_dir, txt_filename)

        # print(f"🔍 변환 중: {filename} → {txt_filename}")

        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)

            # print(f"✅ 저장 완료: {txt_path}")
        except Exception as e:
            print(f"오류 발생: {e} (파일: {filename})")

print("\n 모든 PDF → TXT 변환 완료!")
