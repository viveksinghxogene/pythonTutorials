import threading
print(f'the nae of the current thread is {threading.current_thread().name}')
#we also check if the main thread is in execution
if threading.current_thread()== threading.main_thread():
    print('the main thread is running now.')