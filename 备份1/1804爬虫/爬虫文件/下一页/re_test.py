import re
str = 'aabbccddee'

pattern = re.compile('a')

result = re.match(pattern,str)
print(type(result))
print(result.group())

result = re.finditer(pattern,str)
print(type(result))

for i in result:
    print(type(i))
    print(i.group())

