# import threading
# def saysorry():
#     for i in range(0,5):
#         print('啊 哈哈'+threading.current_thread().name)

# def do():
#     for i in range(0,3):
#         print('么么哒'+threading.current_thread().name)


# if __name__ == '__main__':
#     td1 = threading.Thread(target=saysorry,name='线程一号')
#     td1.start()
#     td2 = threading.Thread(target=do,name='线程二号')
#     td2.start()

#创建进程的两种方式
# from multiprocessing import Pool
# import time,os

# def runtest(num):
#     print('进程开启'+str(os.getpid()))
#     time.sleep(2)

#     print('进程结束'+str(os.getpid()))
#     return num,num

# def done(future):
#     print(future)

# p = Pool(4)
# for i in range(0,50):
#     p.apply_asyns(func=runtest,args=(i,),callbask=done)
# p.close()
# p.join()


#第二种
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import time,os

def runtest(num):
    print('线程开启'+str(os.getpid()))
    time.sleep(2)
    print('线程结束'+str(os.getpid()))
    return num

def done(future):
    print('这是回调函数'+str(future.result()))

pool = ProcessPoolExecutor(4)
for i in range(0,50):
    handle = pool.submit(runtest,(i,))
    handle.add_done_callback(done)

pool.shutdown(wait=True)

