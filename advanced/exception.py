try:
  print('Hello')
except:
  print('Bye')

try:
  print(4 / 0)
except ZeroDivisionError as e:
  print(e)
except IndexError as e2: # 다중 catch가 가능함!
  print(e2)
finally:
  print('Finish')

try:
  f = open('없는 파일', 'r')
except FileNotFoundError:
  pass

def checkIsTruthy(arg):
  if bool(arg) == True:
    return '참'
  else:
    raise 'Falsy'

print(checkIsTruthy(1))
# checkIsTruthy(None) - 에러 발생

class CustomError(Exception):
  def __str__(self): # 오류 메시지가 보이게 하려면 __str__ 메서드를 구현해야 함
    return 'HAHA'

def testFunc(arg):
  if arg == 'Hello':
    raise CustomError()

  print('Haha')

try:
  testFunc('Hello')
except CustomError as e:
  print(e)
