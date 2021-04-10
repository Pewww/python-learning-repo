def add(a, b):
  return a + b

print(add(2, 3))

def say():
  print('Hi!')

say()

def strAdd(str1, str2):
  return str1 + str2

result1 = strAdd('A', 'B')
result2 = strAdd(str2 = 'B', str1 = 'A') # 매개변수 지정 시 순서에 상관없이 사용 가능

print(result1, result2)

def unknownArgs(fist, *args): # * 사용 시 튜플로 모아서 돌려줌
  print(args)

unknownArgs(1, 2, 3)
unknownArgs([1, 2, 3], 4, 5)
unknownArgs((1, 2), (3, 4), 55, [6, 7])

def printKwargs(**kwargs): # 딕셔너리를 반환함
  print(kwargs)

printKwargs(a = 1, b = {'b': 3}) # key = value의 형태로 넘겨줘야함

def addAndMul(a, b):
  return a + b, a * b

res1, res2 = addAndMul(3, 5)

print(res1, res2)

def living(human = True):
  print('인간') if human else print('다른 생물')

living()
living(False)

a = 1

def addA():
  global a
  a += 1

addA()

print(a)

add2 = lambda a, b: a + b

print(add2(7, 5))

defWithNoParam = lambda : print('No parameter')

defWithNoParam()
