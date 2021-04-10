arr = [1, 2, 3]

for i in arr:
  print(i)

arr2 = [(1, 2), (3, 4), (5, 6)]

for (first, second) in arr2:
  print(f'{first} - {second}')

scores = [90, 25, 67, 45, 80]

PASS_SCORE_CRITERIA = 60

for score in scores:
  print('합격') if score >= PASS_SCORE_CRITERIA else print('불합격')

for score in scores:
  if (score >= PASS_SCORE_CRITERIA):
    print('합격')
  else:
    continue

for i in range(1, 10): # 1 이상 10 미만, 처음 생략 시 0부터 시작
  print(i)

total = 0

for i in range(1, 11):
  total += i

print(f'총 점수: {total}')

for idx in range(len(scores)):
  score = scores[idx]
  print(f'점수: {score}')

for i in range(2, 10):
  for j in range(1, 10):
    print(f'{i} x {j} = {i * j}'
     #, end = ' '
    )
  
  print('\n')

a = [1, 2, 3, 4]

result = [num * 3 for num in a] # 좀 기괴하구만..
# [표현식 for 항목 in 반복가능객체 if 조건문]

print(result)

gugu = [x * y for x in range(2, 10)
              for y in range(1, 10)]

print(gugu)
