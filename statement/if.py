money = 2000

if money < 3000:
  print('걸어가야함')
else:
  print('택시타고감')

hasCard = True

if money >= 3000 or hasCard:
  print('택시타고감')
else:
  print('걸어가야함')

print(1 in [1, 2, 3])

print(1 not in [2, 3])

print('a' in ('a', 'b', 'c'))

print('a' not in 'python')

a = 5

if a == 3:
  print(3)
elif a == 5:
  pass
else:
  print(2)

if a == 5: pass
else: print(12)

print(5) if a == 5 else print(12) # 삼항연산자 처럼 사용하면 될 듯
