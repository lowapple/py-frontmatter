import argparse
import datetime
import os
import re

parser = argparse.ArgumentParser(description='폴더 내 파일 이름을 기준으로 YAML Front Matter를 추가합니다.')
parser.add_argument('folder', type=str, help='폴더 경로')
args = parser.parse_args()

folder_path = args.folder

# 해당 폴더 내 모든 파일과 폴더를 리스트로 가져옴
file_list = os.listdir(folder_path)

# 파일 리스트에서 md로 끝나는 파일들만 추출하여 출력
for file_name in file_list:
    if file_name.endswith(".md"):
        with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as md:
            file_title, file_id = file_name.rsplit(' ', 1)
            file_title = file_title.strip()
            file_slug = '/' + file_title.replace(' ', '-').lower()
            file_date = datetime.date.today().strftime("%Y-%m-%d")
            yaml_str = f'---\ntitle: {file_title}\nslug: "{file_slug}"\ndate: {file_date}\n---\n\n'

            # md 파일 내용을 읽어와 YAML Front Matter를 추가한 후, 출력 파일에 쓰기
            with open(os.path.join(folder_path, file_name), "r+", encoding="utf-8") as f:
                md_content = md.read()
                # markdown normalized contents
                md_content = re.sub('[^\x00-\x7F]+', '', md_content)
                f.write(yaml_str + md_content + "\n")
                f.write("\n")
            # 파일이름 공백을 제거하고, 파일명 앞에 날짜를 추가
            new_file_name: str = file_date + '-' + file_title.replace(' ', '-').lower().strip() + '.mdx'
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))