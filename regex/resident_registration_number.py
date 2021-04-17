import re

def masking(data):
  pattern = re.compile('(\d{6})[-]\d{7}')
  return pattern.sub('\g<1>-*******', data)

print(masking('001122-1234567'))
