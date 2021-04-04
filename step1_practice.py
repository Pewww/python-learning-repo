# 1
def average(kor, eng, math):
  return ((kor + eng + math) // 3)

print(average(80, 70, 55))

# 2
def isOdd(num):
  return num % 2 == 1

print('홀수' if isOdd(13) else '짝수')

# 3
registerStr = '881120-1068234'

yy = registerStr[:2]
mm = registerStr[2:4]
dd = registerStr[4:6]

backStr = registerStr[7:]

print(yy, mm, dd, backStr)

# 4
[_, splitedRegisterStr] = registerStr.split('-')

print(splitedRegisterStr[0])

# 5
a = 'a:b:c:d'
replaced = a.replace(':', '#')

print(replaced)

# 6
arr = [1, 3, 5, 4, 2]
sorted = arr.sort(reverse = True)

print(arr)

# 7
strList = ['Life', 'is', 'too', 'short']
joined = ' '.join(strList)

print(joined)

# 8
numTuple = (1, 2, 3)
added = numTuple + (4,)

print(added)

# 9
emptyDict = dict()
# print(emptyDict[[1]]) - 3. Error

# 10
scoreDict = {
  'A': 90,
  'B': 80,
  'C': 70
}

print(scoreDict['B'])

# 11
duplicate = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = list(set(duplicate))

print(unique)

# 12
# b 값도 변경됨 - 같은 주소를 가리키기 때문
aa = bb = [1, 2, 3]
aa[1] = 4
print(aa, bb)
