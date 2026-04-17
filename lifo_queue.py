import queue
lq= queue.LifoQueue()
lq.put("React")
lq.put("AWS")
lq.put("Azure")
print('the queue is as follows: ',lq.queue)
print('the size of the queue is as follows: ',lq.qsize)
