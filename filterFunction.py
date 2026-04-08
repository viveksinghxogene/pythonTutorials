from functools import reduce
l1=[3,78,12,97,8,90,345,60,9982]
evenList=list(filter(lambda x:x%2==0,l1)) #this will do the filtering in the l1 only by passing the argument in the filter function
oddList=list(filter(lambda x:x%2!=0,l1))
print(evenList)
print(oddList)

# double each number in a list
def double(n):
   return n * 2
numbers = [1, 2, 3, 4]
result = map(double, numbers)
print(list(result))


numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product) # mul of each element