from numpy import *

arr = array([1, 2, 3, 4, 5], int)
carr = array(['a', 'b', 'c'])
sarr = array(['Python', 'Django', 'Django Rest'])

print(arr)
print(carr)
print(sarr)

print(linspace(0, 100))

larr = logspace(1, 20)
for i in larr:
    print(i)

print(arange(100, 1, -2))
print(zeros(20, int))
print(ones(10))