import queue


fifo_Queue=queue.PriorityQueue()
fifo_Queue.put(34)
fifo_Queue.put(90)
fifo_Queue.put(12)
fifo_Queue.put(10)
while fifo_Queue.empty() is False:
    print(f'queue element: {fifo_Queue.get()}')