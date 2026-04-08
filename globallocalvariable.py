x=948.43
def printVal():
    x=90.32
    print(f'printing the local value of x: {x}')
    print(f'printing the global value of x: {globals()['x']}')# acccessing the global variable in a function


printVal()