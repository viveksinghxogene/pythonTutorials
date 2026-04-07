a="  you are awesome "
b="""this is the mulitline 
string that automatically contains the 
new line inside itself
and make the best usage of the preformatted text"""

print(a[3])
print(a[0:7])
print(a[:-1])
print(a[0:9:-1])
print(a.strip())
print(a[::-1].strip())
print(a.lstrip())
print(a.rstrip())
print(a.find('awesome',0,len(a)))
print(a.replace('awesome','vivek singh').strip())