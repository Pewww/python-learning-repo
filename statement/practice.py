# 1
결과값: 'shirt'

# 2
total = 0
num = 1

while num <= 1000:
  if (num % 3 == 0):
    total += num
  
  num += 1

print(total)

# 3
cnt = 1

while (cnt <= 5):
  print('*' * cnt)
  cnt += 1

# 4
for i in range(1, 101):
  print(i, end = ' ')

print('\n')

# 5
scores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
avg = 0

for score in scores:
  total += score

avg = total / len(scores)

print(avg)

# 6
numbers = [1, 2, 3, 4, 5]

result = [n * 2 for n in numbers if n % 2 == 1] # 괴랄하다 괴랄해..

print(result)
