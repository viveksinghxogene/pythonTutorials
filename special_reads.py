f = open('3.txt', 'r')

print(f.read(12))

f.seek(0)
print(f.readline(3))

f.seek(0)
print(f.readlines())

f.close()