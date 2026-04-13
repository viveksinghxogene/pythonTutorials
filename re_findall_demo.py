import re
str = "Take up One idea.One idea at a time. AND one idea can change the world if you have powerr to do so."

result = re.search(r'o\w\w', str)
print(result)

result = re.findall(r'o\w\w', str)
print(result)

result = re.match(r'o\w\w', str)
print(result)