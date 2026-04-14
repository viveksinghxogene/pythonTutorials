import queue

#higher the number lower the exit priority
nl_Queue=queue.PriorityQueue()
nl_Queue.put((200,"Vanshika"))
nl_Queue.put((23,"Vivek"))
nl_Queue.put((89,"Ashtosh"))
nl_Queue.put((100,"Deepak"))

while nl_Queue.empty() is False:
    print('Value at the queue is : ',nl_Queue.get())
