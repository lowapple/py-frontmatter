import argparse
import os

parser = argparse.ArgumentParser(description='md 파일 찾기')
parser.add_argument('folder', type=str, help='폴더 경로')
args = parser.parse_args()

folder_path = args.folder

# 해당 폴더 내 모든 파일과 폴더를 리스트로 가져옴
file_list = os.listdir(folder_path)

# 파일 리스트에서 md로 끝나는 파일들만 추출하여 출력
for file_name in file_list:
    if file_name.endswith(".md"):
        print(os.path.join(folder_path, file_name))
