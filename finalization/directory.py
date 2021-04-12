# 하위 디렉터리 검색하기
import os

def search(dirname, ext = '.py'):
  try:
    filenames = os.listdir(dirname)

    for filename in filenames:
      full_filename = os.path.join(dirname, filename)

      if os.path.isdir(full_filename): # 디렉터리일 시
        search(full_filename) # 재귀로 검색
      else:
        extension = os.path.splitext(full_filename)[-1]

        if extension == ext:
          print(full_filename)
  except PermissionError:
    pass

search('./finalization')

# os.walk: 시작 디렉터리부터 시작하여 그 하위 모든 디렉터리를 차례대로 방문하게 해주는 함수이다.
for (path, dir, files) in os.walk('./finalization'):
  for filename in files:
    ext = os.path.splitext(filename)[-1]

    if ext == '.py':
      print(f'{path}{filename}')
