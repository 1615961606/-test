#线程锁：当我们创建多个线程去修改同一个变量的时候，
#可能会造成资源紊乱，当我们修改共享资源的时候，要先加锁，
#修改完毕，解锁．

import threading

num = 0

#实例化一个线程锁
thread_lock = threading.Lock()

def add_num1(number):
    global num
    for _ in range(0,number):
        #加锁，锁定资源，这样，别的线程就无法使用了
        thread_lock.acquire()
        num+=1
        #修改完毕，解锁，这其他线程才能修改资源
        thread_lock.release()


def add_num2(number):
    global num
    for _ in range(0,number):
        #加锁，锁定资源，这样，别的线程就无法使用了
        thread_lock.acquire()
        num+=1
        #修改完毕，解锁，这其他线程才能修改资源
        thread_lock.release()

if __name__ == '__main__':
    #创建线程
    td1 = threading.Thread(target=add_num1,args=(100000,))

    td2 = threading.Thread(target=add_num2,args=(100000,))
    #开启线程
    #开启线程
    td1.start()
    td2.start()

   　#主线程等待子线程执行完毕
    td1.join()
    td2.join()

    print('累加完毕的num值为:',num)

