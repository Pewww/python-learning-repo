s1 = set([1, 2, 3])

print(s1)

s2 = set(['h', 'e', 'l', 'l', 'o'])

print(s2) # unordered

s3 = list(s2)

print(s3)

t1 = tuple(s2)

print(t1)

num1 = set([1, 2, 3, 4, 5, 6])
num2 = set([4, 5, 6, 7, 8, 9])

print(num1 & num2) # 교집합

print(num1.intersection(num2)) # 교집합

print(num1 | num2) # 합집합

print(num1.union(num2)) # 합집합

print(num1 - num2) # 차집합
print(num2 - num1) # 차집합

print(num1.difference(num2)) # 차집합
print(num2.difference(num1)) # 차집합

s1.add(4)
s1.update([5, 6])
s1.remove(6)

print(s1)
