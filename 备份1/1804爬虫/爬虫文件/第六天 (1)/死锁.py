# 由于可以存在多个锁，不同的线程持有不同的锁，
# 并试图获取对方持有的锁时，可能会造成死锁

import threading
import time

# 在线程间共享多个资源的时候，如果两个线程分别
# 占有一部分资源并且同时等待对方的资源，就会造成死锁。
def thread1_do():
    #将lock1上锁
    lock1.acquire()
    time.sleep(1)

    lock2.acquire()
    print('访问local2锁定的资源')
    lock2.release()

def thread2_do():
    #将lock２上锁
    lock2.acquire()
    time.sleep(1)

    lock1.acquire()
    print('访问local1锁定的资源')
    lock1.release()

lock1 = threading.Lock()
lock2 = threading.Lock()

if __name__ == '__main__':
    
    td1 = threading.Thread(target=thread1_do)
    td2 = threading.Thread(target=thread2_do)

    td1.start()
    td2.start()