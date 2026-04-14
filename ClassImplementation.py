from threading import *



class NumberClass:
    def printNumbers(self,num):
        print(f'Current Thread is :{current_thread().name}')
        for i in range(num):
            print(i)


obj1=NumberClass()
obj2=NumberClass()
obj3=NumberClass()


t1=Thread(target=obj1.printNumbers,args=(20,))
t2=Thread(target=obj2.printNumbers,args=(20,))
t3=Thread(target=obj3.printNumbers,args=(20,))

t1.start()
t2.start()

t1.join(10)
t2.join(10)

t3.start()