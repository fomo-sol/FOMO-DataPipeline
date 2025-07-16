import os

# 입력 폴더 및 출력 폴더
txt_dir = "./FOMC_Conference_Transcript/원문txt"
output_dir = "./FOMC_Conference_Transcript"
os.makedirs(output_dir, exist_ok=True)

# 원본 txt 파일들 정렬
txt_files = sorted([f for f in os.listdir(txt_dir) if f.endswith(".txt")])

# 3등분
n = len(txt_files)
chunk_size = n // 3 + (1 if n % 3 else 0)  # 예: 44개면 15,15,14로

chunks = [txt_files[i:i + chunk_size] for i in range(0, n, chunk_size)]

# 저장
for idx, chunk in enumerate(chunks):
    start_date = chunk[0].split("_")[0]
    end_date = chunk[-1].split("_")[0]
    output_filename = f"FOMC_all_trans_en_{start_date}-{end_date}.txt"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, "w", encoding="utf-8") as outfile:
        for filename in chunk:
            date = filename.split("_")[0]
            outfile.write(f"\n\n========== {date} ==========\n\n")

            with open(os.path.join(txt_dir, filename), "r", encoding="utf-8") as infile:
                text = infile.read()
                outfile.write(text)

    print(f"✅ 저장 완료: {output_filename}")
