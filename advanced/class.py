class Calulator:
  def __init__(self):
    self.result = 0

  def add(self, *nums):
    for num in nums:
      self.result += num

    return self.result

cal1 = Calulator()

print(cal1.add(2, 3, 5))

class FourCal:
  def __init__(self): # 생성자 함수
    self.num1 = 0
    self.num2 = 0

  def setdata(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def add(self):
    return self.num1 + self.num2

  def mul(self):
    return self.num1 * self.num2

  def sub(self):
    return self.num1 - self.num2

  def div(self):
    return self.num1 // self.num2

fourCal = FourCal()
fourCal.setdata(6, 3)

print(fourCal.add())
print(fourCal.mul())
print(fourCal.sub())
print(fourCal.div())

a = FourCal()
FourCal.setdata(a, 10, 5)

print(a.add())

class MoreFourCal(FourCal): # 상속
  testValue = 'Hello'

  def pow(self):
    return self.num1 ** self.num2

  def div(self): # 오버라이딩
    if self.num2 == 0:
      return 0
    else:
      return self.num1 // self.num2

b = MoreFourCal()
b.setdata(3, 0)

print(b.pow())
print(b.div())
print(b.testValue)
print(MoreFourCal.testValue)
