a=[34,12,56,879,90,1,567,23,2]
b=[1,2,3,4,5,6,7,8,89]
c=[2,3,4,5,6,7,8,89,10]
z=[a[i]*b[i]*c[i] for i in range(len(a))]
print('the list after multiplication is: ')
print(z)