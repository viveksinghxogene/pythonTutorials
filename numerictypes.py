''' This program tell the usage of numeric types in python
Author : Vivek Singh
Date : 06/04/26
(The muliline comment is only for understanding purpose only
'''
a=90
b=24
c=-634
#these are the integer types that are printed here
print(a,b,c)
a=90.78
l=-34.12
print(a,l)
print(type(l))
#the below are complex type
e=4+16j
print(f'this i shte actual value of e: {e}')
print('this is the real part value of e')
print(e.real)
print('this is the imaginary part value of e')
print(e.imag)
#this is the binary type
a=0b10101
print(a,type(a))
b=0x96AB
c=0xAF89
print('hexadecimal values are as follows:')
print(b,type(b))
print(c,type(c))
#this is the boolean data types
a=True
print(f'the value of boolean data type a is {a}',type(a))
print(type(a)==type(b))