from threading import *
from time import sleep

def printNumbers(n):
    print(f'current thread is :{current_thread().name}')
    sleep(2)
    for i in range(0,n,1):
        print(i)

t1=Thread(target=printNumbers,args=(12,))
t2=Thread(target=printNumbers,args=(12,))
t3=Thread(target=printNumbers,args=(12,))

t1.start()
t2.start()
t3.start()