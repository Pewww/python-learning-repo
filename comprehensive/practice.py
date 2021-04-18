# 1
s = 'a:b:c:d'

print('#'.join(s.split(':')))

# 2
a = {
  'A': 90,
  'B': 80
}

print(70 if not 'C' in a else a['C'])

# 3
# +를 사용할 시 주소 값이 달라진다.

# 4
over_fifty = lambda value: value >= 50

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0

for num in list(filter(over_fifty, A)):
  result += num

print(result)

# 5
def fibo(n):
  if n == 0 or n == 1:
    return n

  return fibo(n - 1) + fibo(n - 2)

print(fibo(6))

# 6
user_input = input()

splited = user_input.split(',')

print(splited)

tot = 0

for val in splited:
  tot += int(val)

print(tot)

# 7
def gugu(dan):
  for i in range(1, 10):
    print(dan * i, end=' ')

gugu(2)

# 8
f = open('./comprehensive/abc.txt', 'r')

splited = f.read().split('\n')
reversed_file = list(reversed(splited))

f2 = open('./comprehensive/abc.txt', 'w')

for string in reversed_file:
  f2.write(string + '\n')

# 9
f3 = open('./comprehensive/sample.txt', 'r')

scores = f3.read().split('\n')
print(scores)

tot = 0

for score in scores:
  tot += int(score)

avg = tot // len(scores)

f4 = open('./comprehensive/sample.txt', 'a')

f4.write(f'\n{tot}, {avg}')

# 10
class Calulator:
  def __init__(self, nums):
    self.nums = nums

  def sum(self):
    self.total = 0

    for num in self.nums:
      self.total += num

    return self.total

  def avg(self):
    return self.total // len(self.nums)

c = Calulator([1, 2, 3, 4, 5])

print(c.sum())
print(c.avg())

# 11
# sys 모듈 사용
# PYTHONPATH 환경 변수 사용
# 현재 디렉터리 사용

# 12
# IndexError 발생, 7 출력

# 13
def is_odd(num):
  return num % 2 == 1

def is_even(num):
  return num % 2 == 0

def dash_insert(string):
  new_str = ''

  for i in range(0, len(string)):
    curr_val = int(string[i])

    new_str += f'{curr_val}'

    if i == len(string[:-1]):
      break

    next_val = int(string[i + 1])

    if is_odd(curr_val) and is_odd(next_val):
      new_str += '-'
    elif is_even(curr_val) and is_even(next_val):
      new_str += '*'
  
  return new_str

print(dash_insert('4546793'))

# 14
def compress(string):
  curr = string[0]
  cnt = 0
  new_str = ''

  for val in string:
    if val != curr:
      new_str += f'{curr}{cnt}'

      curr = val
      cnt = 1
    else:
      cnt += 1

  new_str += f'{curr}{cnt}'

  return new_str

print(compress('aaabbcccccca'))

# 15
def check_duplicate(numStr):
  splited = list(numStr)
  max_splited_len = 10

  if (len(splited) != max_splited_len):
    return False

  total_should_be = 45
  total = 0

  for val in splited:
    total += int(val)

  return total == total_should_be

arr = [
  '0123456789',
  '01234',
  '01234567890',
  '6789012345',
  '012322456789'
]

for val in arr:
  print(check_duplicate(val))

# 16
MORSE_CODES = {
  '.-': 'A',
  '-...': 'B',
  '-.-.': 'C',
  '-..': 'D',
  '.': 'E',
  '..-.': 'F',
  '--.': 'G',
  '....': 'H',
  '..': 'I',
  '.---': 'J',
  '-.-': 'K',
  '.-..': 'L',
  '--': 'M',
  '-.': 'N',
  '---': 'O',
  '.--.': 'P',
  '--.-': 'Q',
  '.-.': 'R',
  '...': 'S',
  '-': 'T',
  '..-': 'U',
  '...-': 'V',
  '.--': 'W',
  '-..-': 'X',
  '-.--': 'Y',
  '--..': 'Z'
}

morse_code = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'

splited_morse = morse_code.split('  ')
fin = ''

for word in splited_morse:
  letters = word.split(' ')
  
  for letter in letters:
    fin += MORSE_CODES[letter]
  
  fin += ' '

print(fin)

# 17
# 2번

# 18
# 10

# 19
import re

phone = '''
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
'''

pat = re.compile('(\d{3}[-]\d{4})[-]\d{4}')
result2 = pat.sub('\g<1>-####', phone)

print(result2)

# 20
pat2 = re.compile('.*[@].*[.](?=com$|net$).*$')

print(pat2.match('park@naver.com'))
print(pat2.match('park@naver.kr'))
