def average(a,b,c):
    print(f'The average of the three number is : {float((a+b+c)/3)}')

average(56,34,88)

def avgwithresult(a,b,c):
    return float((a+b+c)/3)

a,b,c=23,89,12
print(f'the avg of {a,b,c} is: {avgwithresult(a,b,c)}')