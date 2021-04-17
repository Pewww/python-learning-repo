# 메타 문자
# 앞에서 살펴본 +, *, [ ], { } 등의 메타 문자는 매치가 진행될 때
# 현재 매치되고 있는 문자열의 위치가 변경된다. (보통 소비된다고 표현함)
# 이와 달리 문자열을 소비시키지 않는 메타 문자도 있는데 한 번 살펴보자.

# I
# I 메타 문자는 or과 동일한 의미로 사용된다.
# A|B라는 정규식이 있다면 A 또는 B라는 의미가 된다.
import re

p = re.compile('Crow|Servo')
m = p.match('CrowHello')

print(bool(m)) # True

# ^
# ^ 메타 문자는 문자열의 맨 처음과 일치함을 의미한다.
# 앞에서 살펴봤던 컴파일 옵션 re.MULTILINE을 사용할 경우에는 여러 줄이 문자열일 때 각 줄의 처음과 일치하게 된다.

print(re.search('^Life', 'Life is too short')) # Match Object
print(re.search('^Life', 'My Life')) # None

# $
# ^ 메타 문자와 반대의 경우이다.
# $는 문자열의 끝과 매치함을 의미한다.

print(re.search('short$', 'Life is too short')) # Match Object
print(re.search('short$', 'Life is too long')) # None

# \A
# \A는 문자열의 처음과 매치됨을 의미한다.
# ^ 메타 문자와 동일한 의미이지만 re.MULTILINE 옵션을 사용할 경우에는 다르게 해석된다.
# re.MULTILINE 옵션 사용 시 ^은 각 줄의 문자열의 처음과 매치되지만,
# \A는 줄과 상관없이 전체 문자열의 처음하고만 매치된다.

# \Z
# \Z는 문자열의 끝과 매치됨을 의미한다.
# \A와 동일하게 re.MULTILINE 사용 시 전체 문자열의 끝과 매치된다.

# \b
# \b는 단어 구분자(Word boundary)이다.
# 보통 단어는 whitespace에 의해 구분된다.
p2 = re.compile(r'\bclass\b')

print(p2.search('no class at all')) # Match Object
print(p2.search('one subclass is')) # None

# \b는 파이썬 리터럴 규칙에 따라 백스페이스를 의미하므로,
# 단어 구분자임을 알려주기 위해 기호 r을 반드시 붙여줘야 한다.

# \B
# \B 메타 문자는 \b 메타 문자와 반대의 경우이다.
# 즉 whitespace로 구분된 단어가 아닌 경우에만 매치된다. (앞 뒤에 whitespace가 하나라도 있는 경우에는 매치 X)

p3 = re.compile(r'\Bclass\B')

print(p3.search('no class at all')) # None
print(p3.search('declassified algorithm')) # Match Object

# 그루핑
# 보통 반복되는 문자열을 찾을 때 그룹을 사용하는데,
# 보다 큰 이유는 매치된 문자열 중에서 특정 부분의 문자열만 뽑아내기 위함이다.

p4 = re.compile('(ABC)+')

print(p4.search('ABCABCab')) # Match Object

p5 = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
m2 = p5.search('jung 010-7298-5257')

print(m2.group(1)) # jung

# 이름에 해당하는 \w+ 부분을 그룹 (\w+)으로 만들면 match 객체의 group(인덱스) 메서드를 사용하여
# 그루핑된 부분의 문자열만 뽑아낼 수 있다.
# group 메서드의 인덱스는 다음과 같은 의미를 갖는다.

# group(0): 매치된 전체 문자열
# group(n): n번째 그룹에 해당되는 문자열

# 그루핑된 문자열 재참조하기
# 그룹의 또 하나 좋은 점은 한 번 그루핑한 문자열을 재참조할 수 있다는 점이다.

p6 = re.compile(r'(\b\w+)\s+\1')
print(p6.search('Paris is in the the spring').group())

# 정규식 (\b\w+)\s\1은 (그룹) + " " + 그룹과 동일한 단어와 매치됨을 의미한다.
# 이렇게 정규식을 만들게 되면 2개의 동일한 단어를 연속적으로 사용해야만 매치된다.
# 이것을 가능하게 해주는 것이 바로 재참조 메타 문자인 \1이며, \1은 정규식의 그룹 중 첫 번째 그룹을 가리킨다.

# 그루핑된 문자열에 이름 붙이기
# 정규식 안에 그룹이 많아질 경우 매우 혼란스러워진다.
# 이런 경우 그룹을 인덱스가 아닌 이름으로 참조할 수 있는데, 방법은 아래와 같다.

# (?P<그룹명>...)

# (?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
# 기존과 달라진 부분은 (\w+) -> (?P<name>\w+) 이며,
# 가독성이 떨어지긴 하지만 명칭에 대한 강력함을 갖게 된다.

p7 = re.compile(r'(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)')
m3 = p7.search('jung 010-7298-5257')

print(m3.group('name')) # jung

# 그룹 이름을 사용하면 정규식 안에서 재참조하는 것도 가능하다. (?P=그룹이름)

# 전방 탐색
# 정규식 안에 해당 확장 구문을 사용하면 순식간에 암호문처럼 알아보기 어렵게 바뀐다.
# 하지만 꼭 필요한 경우가 있고 매우 유용한 경우도 많으니 꼭 알아두자.

p8 = re.compile('.+:')
m4 = p8.search('http://google.com')

print(m4.group()) # 'http:'

# 만약 http:라는 검색 결과에서 :을 제외하고 출력하고 싶을 때 전방 탐색을 사용한다면?
# 전방 탐색은 긍정과 부정 2종류가 있고 다음과 같이 표현한다.

# 긍정형 전방 탐색(?=...): ...에 해당되는 정규식과 매치되어야 하며 조건이 통과되어도 문자열이 소비되지 않는다.
# 부정형 전방 탐색(?!...): ...에 대항되는 정규식과 매치되지 않아야 하며 조건이 통과되어도 문자열이 소비되지 않는다.

# 긍정형 전방 탐색
# 긍정형 전방 탐색을 사용하면 http:의 결과를 http로 바꿀 수 있다.

p9 = re.compile('.+(?=:)') # :에 해당하는 문자열이 검색에는 포함되지만 검색 결과에는 제외된다.
m5 = p9.search('http://google.com')

print(m5.group()) # 'http'

# .*[.].*$ 정규식은 파일 이름 + . + 확장자를 나타내는 정규식이다.
# 이 정규식에 확장자가 bat인 파일을 제외해야 한다라는 조건이 추가된다면,
# .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$ 와 같이 변경해야 할 것이다.

# 그런데 여기에서 bat 파일말고 exe 파일도 제외하라는 조건이 추가로 생긴다면 정규식은 훨씬 복잡해진다.

# 부정형 전방 탐색
# 이럴 때 유용하게 사용할 수 있는 것이 바로 부정형 전방 탐색이다.
# 부정형 전방 탐색을 사용할 시 .*[.](?!bat$).*$ 로 간단히 축약되며,
# 아까와 같이 exe 확장자 역시 제외한다는 조건이 추가된다면 .*[.](?!bat$|exe$).*$ 처럼 표현하면 된다.

# 문자열 바꾸기
# sub 메서드를 사용하면 정규식과 매치되는 부분을 다른 문자로 쉽게 바꿀 수 있다.

p10 = re.compile('(blue|white|red)')

print(p10.sub('color', 'blue socks and red shoes')) # color socks and color shoes

# 비꾸기 횟수를 제어하려면 세 번째 인자로 count를 넘기면 된다.

print(p10.sub('color', 'blue socks and red shoes', count=1)) # color socks and red shoes

# subn 메서드도 sub 메서드와 유사하지만 반환 결과를 튜플로 돌려주며, (변경된 문자열, 변경 횟수)의 형태를 지닌다.

# sub 메서드 사용 시 참조 구문 사용하기
# sub 메서드를 사용할 때 참조 구문을 사용할 수 있다.

p11 = re.compile(r'(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)')
print(p11.sub('\g<phone> \g<name>', 'jung 010-7298-5257')) # 010-7298-5257 jung

# sub 메서드의 매개변수로 함수 넣기
# sub 메서드의 첫 번째 인자로 함수를 넣을 수도 있다.

def hexrepl(match):
  value = int(match.group())
  return hex(value)

p12 = re.compile(r'\d+')
print(p12.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
# 'Call 0xffd2 for printing, 0xc000 for user code.'

# Greedy vs Non-Greedy

s = '<html><head><title>Title</title>'
print(len(s)) # 32
print(re.match('<.*>', s).span()) # (0, 32)
print(re.match('<.*>', s).group()) # <html><head><title>Title</title>

# <.*> 정규식의 매치 결과로 <html> 문자열을 돌려주길 기대했지만,
# * 메타 문자는 매우 탐욕스러워서 매치할 수 있는 최대 문자열을 반환하였다.
# 이 탐욕스러움을 제한하기 위해 non-greedy 문자인 ?를 사용할 수 있는데,

print(re.match('<.*?>', s).group()) # <html>

# 형식은 위와 같으며, ?는 *?, +?, ??, {m,n}? 와 같이 사용할 수 있다.
# 가능한 한 가장 최소한의 반복을 수행하도록 도와주는 역할을 한다.
