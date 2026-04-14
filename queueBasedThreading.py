import random
import time
import queue
from threading import *

def produce(q):
    while True:
        print('Producing')
        q.put(random.randint(1,100))
        print('Produced')
        time.sleep(3)
def consumer(q):
    while True:
        print('Consuming')
        print('Consumed data is: ',q.get())
        time.sleep(1)

q=queue.Queue()
t1=Thread(target=produce,args=(q,))
t2=Thread(target=consumer,args=(q,))
t1.start()
t2.start()