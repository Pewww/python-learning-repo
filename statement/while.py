a = 0
arr = []

while a < 10:
  a += 1

  if a % 2 == 0:
    arr.append(a)
  
  if a == 9:
    break

print(arr)
