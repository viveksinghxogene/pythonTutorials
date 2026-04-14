from threading import *
#implemetnation of thred using a class that extends Thread class of threading library
class ThreadDemo(Thread):
    def run(self):
        print(f'The current thread is : {current_thread().name}')
        for i in range(10):
            print(i)

t1=ThreadDemo()
t1.start()
