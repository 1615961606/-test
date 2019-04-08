#线程锁：当我们创建多个线程取修改同一个变量的时候，
# 可能会造成资源紊乱,当我们修改资源的时候，要先加锁
# 修改完毕，解锁
import threading
num = 0

thread_lock = threading.Lock()
def add_num1(number):
    global num
    for o in range(0,number):
        thread_lock.acquire()
        num += 1
        thread_lock.release()

def add_num2(number):
    global num
    for i in range(0,number):
        thread_lock.acquire()
        num += 1
        thread_lock.release()


if __name__ == '__main__':
    td1 = threading.Thread(target=add_num1,args=(500000,))
    td2 = threading.Thread(target=add_num2,args=(500000,))

    td1.start()
    td2.start()

    td1.join()
    td2.join()
    print('累加完毕的num值为',num)