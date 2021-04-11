# r: 읽기 모드 - 파일을 읽기만 할 때
# w: 쓰기 모드 - 파일에 내용을 쓸 때
# a: 추가 모드 - 파일의 마지막에 새로운 내용을 추가할 떄

f = open('./i.o/New File.txt', 'w') # open(directory, type)

for i in range(1, 11):
  data = f'{i}번째 줄입니다.\n'
  f.write(data)

f.close()

f2 = open('./i.o/New File.txt', 'r')
while True:
  line = f2.readline() # 더이상 읽을 줄이 없을 시 빈 문자열을 리턴함
  if not line: break
  print(line)

f2.close()

f3 = open('./i.o/New File.txt', 'r')
lines = f3.readlines()

for line in lines:
  print(line)

f3.close()

f4 = open('./i.o/New File.txt', 'r')
data = f4.read() # 파일 내용 전체를 문자열로 돌려줌

print(data)

f5 = open('./i.o/New File.txt', 'a')
for i in range(11, 20):
  data = f'{i}번째 줄입니다.\n'
  f5.write(data)

f5.close()

with open('./i.o/New File.txt', 'r') as f6:
  data = f6.read()
  print(data)
