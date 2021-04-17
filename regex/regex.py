# . ^ $ * + ? { } [ ] \ | ( )
# 정규 표현식에 위 메타 문자를 사용하면 특별한 의미를 갖게 된다.
# 메타 문자: 원래 그 문자가 가진 뜻이 아닌 특별한 용도로 사용하는 문자를 말한다.

# 문자 클래스 [ ]
# 문자 클래스로 만들어진 정규식은 "[ ] 사이의 문자들과 매치"라는 의미를 갖는다.

# 정규 표현식이 [abc]라면 이 표현식의 의미는 "a, b, c 중 한 개의 문자와 매치"를 뜻한다.
import re

print(bool(re.match('[abc]', 'a'))) # True
print(bool(re.match('[abc]', 'before'))) # True
print(bool(re.match('[abc]', 'dude'))) # False

# [ ] 안의 두 문자 사이에 하이픈(-)을 사용하면 두 문자 사이의 범위를 의미한다.
# [a-c]라는 정규 표현식은 [abc]와 동일하고 [0-5]는 [012345]와 동일하다.
# [a-zA-Z]: 알파벳 모두, [0-9]: 숫자

# [ ] 안에는 어떤 문자나 메타 문자도 사용할 수 있지만 주의해야 할 메타 문자가 1가지 있다.
# 바로 ^ 인데, 문자 클래스 안에 ^ 메타 문자를 사용할 경우에는 반대(not)의 의미를 갖는다.
# 예를 들어 [^0-9]라는 정규표현식은 숫자가 아닌 문자만 매치된다.

print(bool(re.match('[0-9]', '10'))) # True
print(bool(re.match('[^0-9]', '10'))) # False

# 자주 사용하는 문자 클래스
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자 + 숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자 + 숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

# Dot(.)
# 정규 표현식의 Dot(.) 메타 문자는 줄바꿈 문자인 \n을 제외한 모든 문자와 매치됨을 의미한다.
# 다만, re.DOTALL 옵션을 주면 \n 문자와도 매치된다.

# a.b 정규식의 의미는 "a + 모든 문자 + b"와 같다.

print(bool(re.match('a.b', 'a0b'))) # True
print(bool(re.match('a.b', 'aabbbb'))) # True
print(bool(re.match('a.b', 'abc'))) # False

# a[.]b 정규식의 의미는 "a + Dot(.)문자 + b"

print(bool(re.match('a[.]b', 'a.b'))) # True
print(bool(re.match('a[.]b', 'acb'))) # False

# 반복(*)
# * 바로 앞에 있는 문자가 0부터 무한대로 반복될 수 있다. (정확히는 메모리 제한으로 인해 2억개 정도만 가능하다고 한다.)

print(bool(re.match('ca*t', 'ct'))) # True
print(bool(re.match('ca*t', 'cat'))) # True
print(bool(re.match('ca*t', 'caaaaaaaaat'))) # True

# 반복(+)
# *과 비슷하지만 +는 최소 1번 이상 반복될 때 사용한다.

print(bool(re.match('ca+t', 'ct'))) # False
print(bool(re.match('ca+t', 'cat'))) # True

# 반복({m, n}, ?)
# 반복 횟수를 3회만, 혹은 1회부터 3회까지만 제한하고 싶은 것 처럼 반복 횟수를 고정할 때 사용한다.
# {1,}은 +와 동일하고, {0,}은 *와 동일하다.

# {m}
# 반드시 a가 2번 반복되어야 함

print(bool(re.match('ca{2}t', 'caat'))) # True

# {m, n}
# a가 2 ~ 5회 반복되어야 함

print(bool(re.match('ca{2,5}t', 'caat'))) # True
print(bool(re.match('ca{2,5}t', 'caaaaat'))) # True
print(bool(re.match('ca{2,5}t', 'caaaaaat'))) # False

# ?
# {0, 1}의 의미를 가진다. Boolean의 성격이라고 볼 수 있다.

print(bool(re.match('ca?t', 'cat'))) # True
print(bool(re.match('ca?t', 'ct'))) # True


# 파이썬은 정규 표현식을 지원하기 위해 re 모듈(파이썬을 설치할 때 자동으로 설치되는 기본 라이브러리)을 제공한다.
# re.compile을 통해 반환받은 컴파일된 패턴 객체는 4가지 메서드를 제공한다.

# match(): 문자열의 처음부터 정규식과 매치되는지 조사한다.
# search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려준다.
# finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려준다.

# match, search는 정규식과 매치될 때는 match 객체를 돌려주고, 매치되지 않을 때는 None을 돌려준다.

p = re.compile('[a-z]+')

result = p.findall('Life is too short')
print(result) # ['Life', 'is', 'too', 'short']

result2 = p.finditer('Life is too short')
print(result2) # iterator object

# match와 search 메서드를 수행한 결과로 돌려준 match 객체에 대해 더 살펴보자.
# match 객체의 메서드들은 아래와 같다.

# group(): 매치된 문자열을 돌려준다.
# start(): 매치된 문자열의 시작 위치를 돌려준다.
# end(): 매치된 문자열의 끝 위치를 돌려준다.
# span(): 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.

m = p.match('python')

print(m.group()) # 'python'
print(m.start()) # 0
print(m.end()) # 6
print(m.span()) # (0, 6)


# 컴파일 옵션

# DOTALL(S) - .이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다.)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들 수 있고 주석 등을 사용할 수 있게 된다.)

# 옵션을 사용할 때 re.DOTALL 처럼 전체 옵션 이름을 써도 되고 re.S 처럼 약어를 써도 된다.

pattern = re.compile('a.b')
matched = pattern.match('a\nb')

print(bool(matched)) # False

pattern_with_dotall = re.compile('a.b', re.DOTALL)
matched2 = pattern_with_dotall.match('a\nb')

print(bool(matched2)) # True

p2 = re.compile('[a-z]')
m2 = p2.match('ABc')

print(bool(m2)) # False

p3 = re.compile('[a-z]', re.IGNORECASE)
m3 = p3.match('ABc')

print(bool(m3)) # True

p4 = re.compile("^python\s\w+")

data = '''python one
life is too short
python two
you need python
python three'''

print(p4.findall(data)) # ['python one']

p5 = re.compile("^python\s\w+", re.MULTILINE)

print(p5.findall(data)) # ['python one', 'python two', 'python three']

before_charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

# re.VERBOSE 옵션을 사용하면 문자열에 사용된 whitespace는 컴파일할 때 제거된다.
# 단 [ ] 안에 사용한 whitespace는 제외, 줄 단위로 # 기호를 사용하여 주석을 작성할 수 있다.
after_charref = re.compile(r'''
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
''', re.VERBOSE)


# 백슬래시 문제
# 어떤 파일 안에 있는 '\section' 문자열을 찾기 위한 정규식을 만든다고 가정해보자.
# \section 정규식은 \s 문자가 whitespace로 해석되어 의도한 대로 매치가 이뤄지지 않는다.
# 따라서 의도한 대로 매치하고 싶다면 \\section과 같이 정규식을 변경해야 한다.

pat = re.compile('\\section')

# 여기서 또 하나의 문제가 발견되는데, 위처럼 정규식을 만들어서 컴파일하면 실제 파이썬 정규식 엔진에는
# 파이썬 문자열 리터럴 규칙에 따라 \\이 \로 변경되어 \section이 전달된다.
# 결국 정규식 엔진에 \\ 문자를 전달하려면 파이썬은 \\\\처럼 백슬래시를 4개나 사용해야 한다.

# 이런 경우 r 문자를 사용할 수 있는데, r 문자를 삽입하면 정규식은 Raw String 규칙에 의하여
# 백슬래시 2개 대신 1개만 써도 2개를 쓴 것과 동일한 의미를 갖게된다.

# Before
pat2 = re.compile('\\\\section')

# After
pat2 = re.compile(r'\\section')
