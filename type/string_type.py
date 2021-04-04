str1 = 'He said, "Title is description.".'
str2 = "He's nice."
str3 = '''
Hello
World!
'''
str4 = """
Hello
World!
"""

print(str1)
print(str2)
print(str3)
print(str4)

head = "Python"
tail = " is hot!"

print(head + tail)

a = "python"
print(a * 2)

aLen = len(a)
print(aLen)
print(a[aLen - 1])
print(a[-1])

print(a[0:aLen])
print(a[0:])

b = "20210318Spring"
year = b[:4]
day = b[4:8]
season = b[8:]

print(year, day, season)

c = "pithon"
print(c[0] + "y" + c[2:])

d = "I eat %d apples"
print(d % 3)

e = "I eat %s apples"
print(e % "five")

f = "I eat %d %s apples"
print(f % (2, "big"))

g = "Complete: %d%%"
print(g % 100)

h = 3.141592
print("%0.4f" % h)

i = "I eat {0} {1} apples{mark}".format(3, "small", mark = "!")
print(i)

print("{0:>10}".format("hello"))

name = "Pewww"
age = 22
print(f"나는 {name}, 나이는 {age}")

obj = {
  "name": "Pewww",
  "age": 22
}
print(f'나는 {obj["name"]}, 나이는 {obj["age"]}')

str5 = "ssssssstr"
print(str5.count("s"))
print(str5.find("s"));
print(str5.find("a"))
# print(str5.index("a")) -> Error
print(",".join(str5))
print(str5.upper())
print(str5.upper().lower())

str6 = " " + str5 + " "
print(str6.lstrip())
print(str6.rstrip())
print(str6.strip())

replaceStr = "a a b c"
print(replaceStr.replace("a", "hi"))
print(replaceStr.split())
