import threading
import time
def thread_do1():
    lock1.acquire()
    time.sleep(1)
    lock2.acquire()
    print('锁定的资源')
    lock2.release()
def thread_do2():
    lock2.acquire()
    time.sleep(1)

    lock1.acquire()
    print('锁定的资源')
    lock1.release()

lock1 = threading.Lock()
lock2 = threading.Lock()

if __name__ == '__main__':
    td1 = threading.Thread(target=thread_do1)
    td2 = threading.Thread(target=thread_do2)