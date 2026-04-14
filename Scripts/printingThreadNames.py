from threading import *

def printNumbers(num):
    print(f'the current thread that is runnning is: {current_thread().name}')
    for i in range(num):
        print(i)
print(f'the current thread that is runnning is: {current_thread().name}')
t1=Thread(target=printNumbers,args=(34,))
t1.start()


