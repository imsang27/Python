import os
import shutil

"""
지정된 경로에 파일을 슬라이싱하여 하위 디렉토리를 생성하고 파일을 이동합니다.
폴더는 제외하며, 지정된 문자를 파일 이름에서 삭제합니다.

Args:
	file_path: 파일의 절대 경로
	slice_chars: 파일 이름을 나눌 문자들 (문자열)
	destination_dir: 파일을 이동할 최상위 디렉토리 (생략 가능)
	delete_chars: 파일 이름에서 삭제할 문자들 (문자열) (생략 가능)
"""

def get_user_input():
    path = input("1. 처리할 파일들이 있는 경로를 입력하세요: ")
    delimiters = input("3. 슬라이싱할 기준이 될 문자들을 입력하세요 (콤마로 구분): ").split(',')
    chars_to_remove = input("4. 파일 이름에서 삭제할 문자를 입력하세요 (콤마로 구분, 생략 가능): ").split(',')
    return path, delimiters, chars_to_remove

def remove_chars(filename, chars_to_remove):
    for char in chars_to_remove:
        filename = filename.replace(char, '')
    return filename

def process_files(path, delimiters, chars_to_remove):
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            filename = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]
            
            # 지정된 문자 제거
            filename = remove_chars(filename, chars_to_remove)
            
            # 파일 이름 슬라이싱
            parts = [filename]
            for delimiter in delimiters:
                new_parts = []
                for part in parts:
                    new_parts.extend(part.split(delimiter))
                parts = new_parts
            
            # 새 경로 생성
            new_path = path
            for part in parts[:-1]:
                new_path = os.path.join(new_path, part)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
            
            # 파일 이동
            new_filename = parts[-1] + extension
            new_full_path = os.path.join(new_path, new_filename)
            shutil.move(full_path, new_full_path)
            print(f"Moved: {full_path} -> {new_full_path}")

def main():
  try:	
    path, delimiters, chars_to_remove = get_user_input()
    process_files(path, delimiters, chars_to_remove)
    print("파일 정리가 완료되었습니다.")
  except Exception as e:
    print("오류 발생:", e)	

if __name__ == "__main__":
    main()





# def get_user_input():
#     path = input("경로를 입력하세요: ")
#     delimiters = input("슬라이싱할 기준이 될 문자들을 입력하세요 (콤마로 구분): ").split(',')
#     chars_to_remove = input("파일 이름에서 삭제할 문자를 입력하세요 (콤마로 구분, 생략 가능): ").split(',')
#     return path, delimiters, chars_to_remove

# def remove_chars(filename, chars_to_remove):
#     for char in chars_to_remove:
#         filename = filename.replace(char, '')
#     return filename

# def process_file(file_path, delimiters, chars_to_remove):
#     directory, filename = os.path.split(file_path)
#     filename = remove_chars(filename, chars_to_remove)
    
#     parts = [filename]
#     for delimiter in delimiters:
#         new_parts = []
#         for part in parts:
#             new_parts.extend(part.split(delimiter))
#         parts = new_parts
    
#     new_path = directory
#     for part in parts[:-1]:
#         new_path = os.path.join(new_path, part)
#         os.makedirs(new_path, exist_ok=True)
    
#     new_file_path = os.path.join(new_path, parts[-1])
#     shutil.move(file_path, new_file_path)
#     print(f"파일을 이동했습니다: {new_file_path}")

# def main():
#     path, delimiters, chars_to_remove = get_user_input()
    
#     if os.path.isfile(path):
#         process_file(path, delimiters, chars_to_remove)
#     elif os.path.isdir(path):
#         for root, _, files in os.walk(path):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 process_file(file_path, delimiters, chars_to_remove)
#     else:
#         print("유효하지 않은 경로입니다.")

# if __name__ == "__main__":
#     main()