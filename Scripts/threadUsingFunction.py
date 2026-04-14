from threading import Thread

def printThreadDemo(num):
    print(f'this function is called through thread and will print the number to {num}.')
    for i in range(0,num,1):
        print(i)

t=Thread(target=printThreadDemo,args=(32,))
t.start()