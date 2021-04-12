# m: 총 게시물 수, n: 한 페이지에 보여줄 게시물 수
def getTotalPage(m, n):
  if m % n == 0:
    return m // n
  else:
    return m // n + 1

print(getTotalPage(10, 5))
print(getTotalPage(10, 3))
