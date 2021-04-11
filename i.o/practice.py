# 1
def is_odd(num):
  return num % 2 == 1

print('홀수') if is_odd(5) else print('짝수')

# 2
def getAvg(*nums):
  total = 0

  for num in nums:
    total += num

  return total // len(nums)

print(getAvg(60, 80, 100, 70, 90))

# 3
input1 = input('첫번째 숫자를 입력하세요: ')
input2 = input('두번째 숫자를 입력하세요: ')

total = int(input1) + int(input2)

print('두 수의 합은 %s 입니다.' % total)

# 4
# 3번의 출력 결과가 다름

# 5
f1 = open('./i.o/test.txt', 'w')
f1.write('Life is too short')

f1.close()

f2 = open('./i.o/test.txt', 'r')
print(f2.read())

# 6
with open('./i.o/test.txt', 'a') as f3:
  data = input('내용을 입력하세요: ')
  f3.write('\n' + data)

# 7
f5 = open('./i.o/test2.txt', 'r')
data = f5.readlines()
newData = []

for s in data:
  newData.append(s.replace('java', 'python'))

print(data, newData)

f6 = open('./i.o/test2.txt', 'w')
f6.writelines(newData)
