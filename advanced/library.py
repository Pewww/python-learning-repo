# sys: 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
import sys
print(sys.argv)
print(sys.path) # 파이썬 모듈들이 저장되어 있는 위치

# pickle: 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈이다.
import pickle

f = open('./advanced/test.txt', 'wb')

data = {
  1: 'python',
  2: 'you need'
}
pickle.dump(data, f) # 딕셔너리 객체인 data를 그대로 파일에 저장함

f.close()

f2 = open('./advanced/test.txt', 'rb')

data2 = pickle.load(f2) # 딕셔너리 상태 그대로 불러옴
print(data2)

# os: 환경 변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해준다.
import os

print(os.environ) # 내 시스템의 환경 변수 값
# chdir - 디렉터리 위치 변경
# getcwd - 디렉터리 위치 돌려받기
# system - 시스템 명령어 호출하기
# popen - 실행한 시스템 명령어의 결과값 돌려받기
# mkdir - 디렉터리 생성
# rmdir - 디렉터리 삭제 (디렉터리가 비어있어야 함)
# unlink - 파일을 지움
# rename - 파일 이름 변경

# shutil: 파일을 복사해주는 파이썬 모듈이다.
import shutil
shutil.copy('./advanced/test.txt', './advanced/clone.txt')

# glob: 특정 디렉터리에 있는 파일 이름을 모두 알려준다.
import glob
directories = glob.glob('./advanced/*')

print(directories)

# tempfile: 파일을 임시로 만들어서 사용할 때 유용하다.
import tempfile

filename = tempfile.mkstemp() # 중복되지 않는 임시 파일 이름을 무작위로 만들어서 돌려줌
# TemporaryFile - 임시 저장 공간으로 사용할 파일 객체를 돌려줌
print(filename)

# time: 시간과 관련된 모듈이다.
import time

print(time.time()) # 현재 시간을 실수 형태로 돌려준다.
print(time.localtime()) # 연도, 월, 일, 시...의 형태로 바꿔서 돌려준다.
# asctime - time.localtime에 의해 반환된 튜플 형태의 값을 인수로 받아 쉬운 형태로 돌려준다.
# ctime - asctime과 반환 값은 동일하지만 현재 시간만을 기준으로 한다.
# strftime - 시간과 관련된 여러가지 포맷 코드를 제공한다.
# sleep - 일정한 시간 간격을 두고 구문을 실행할 수 있다. 동기적인 setTimeout 느낌

# calendar: 달력을 볼 수 있게 해주는 모듈이다.
import calendar

print(calendar.calendar(2015)) # 그 해의 전체 달력을 볼 수 있다.
print(calendar.prcal(2015)) # 위와 동일하다.
print(calendar.prmonth(2015, 12)) # 12월의 달력만 보여준다.
# weekday - 그 날짜에 해당하는 요일 정보를 돌려준다.
# monthrange - 입력받은 달의 1일이 무슨 요일인지와 며칠까지 있는지를 튜플 형태로 돌려준다.

# random: 난수를 발생시키는 모듈이다.
import random

print(random.random())
print(random.randint(1, 10)) # 1과 10 사이의 난수

# webbrowser: 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.
import webbrowser

webbrowser.open('https://www.naver.com')
