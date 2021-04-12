# 1
class Calulator:
  def __init__(self):
    self.value = 0

  def add(self, val):
    self.value += val

class UpgradeCalulator(Calulator):
  def minus(self, val):
    self.value -= val

cal = UpgradeCalulator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 2
class MaxLimitCalculator(Calulator):
  max_value = 100

  def add(self, val):
    value = self.value + val
    
    if value > self.max_value:
      self.value = self.max_value
    else:
      self.value = value

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)

print(cal2.value)

# 3
print(all([1, 2, abs(-3)-3])) # False
print(chr(ord('a')) == 'a') # True

# 4
filter_minus = lambda value: value > 0
arr = [1, -2, 3, -5, 8, -3]

print(list(filter(filter_minus, arr)))

# 5
print(int(0xea))

# 6
mul_three = lambda value: value * 3
arr2 = [1, 2, 3, 4]

print(list(map(mul_three, arr2)))

# 7
arr3 = [-8, 2, 7, 5, -3, 5, 0, 1]
print(min(arr3))

# 8
result = 17 / 3
print(round(result, 4))

# 9
import sys

numbers = sys.argv[1:]

result = 0
for num in numbers:
  result += int(num)

print(result)

# 10
import os
os.chdir('./advanced')

result = os.popen('dir')

print(result.read())

# 11
import glob
print(glob.glob('./advanced/*.py'))

# 12
import time

local_time = list(time.localtime())

year = local_time[0]
month = local_time[1]
date = local_time[2]
hour = local_time[3]
minute = local_time[4]
second = local_time[5]

now = f'{year}/{month}/{date} {hour}:{minute}:{second}'

print(now)

# 13
import random

def lotto():
  arr = []

  while len(arr) < 6:
    num = random.randint(1, 45)

    if not num in arr:
      arr.append(num)

  return arr

print(lotto())
