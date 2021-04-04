dic = {
  'name': 'pewww',
  'age': 22
}

print(dic)

dic2 = {
  'names': ['aa', 'bb', 'cc'],
  'inner': {
    'name': 'dd'
  }
}

print(dic2)
print(dic2['names'][:2])

dic2Keys = dic2.keys()

print(dic2Keys) # dict_keys 객체 -> 메모리 낭비를 줄이기 위해 3.0 버전 이후부터 수정됨
print(list(dic2Keys)) # 배열

for k in dic2Keys:
  print(f'key: {k}')

dic2Items = dic2.items()

print(dic2Items) # key와 value 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
print(list(dic2Items))

# dic2.clear() -> 초기화

# print(dic2['outer']) Key 오류 발생
print(dic2.get('outer')) # None 반환
print(dic2.get('outer') == None)
print('outer' in dic2)
