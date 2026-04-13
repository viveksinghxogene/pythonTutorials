import re
str = "Take up One idea.One idea at a Time"

result = re.search(r'o\w', str)
print(result)

result = re.findall(r'o\w\w', str)
print(result)

result = re.match(r'T\w\w', str)
print(result.group())

result = re.sub(r'One', 'Two', str)
print(result)
result = re.match(r'T\w\w', str)
print(result.group())

result = re.sub(r'One', 'Two', str)
print(result)

result = re.findall(r'o\w{1,2}', str)
print(result)

result = re.split(r'\d+', str)
print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)

result = re.search(r'^T', str)
print(result.group())