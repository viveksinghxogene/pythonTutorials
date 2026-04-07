a=89
b=89
#because python point the varibale whose value are same in same memory location
# and the id tells the memory location where the variablesvalue is stored
print(a is b)
print(id(a))
print(id(b))
b=34
print(id(b))