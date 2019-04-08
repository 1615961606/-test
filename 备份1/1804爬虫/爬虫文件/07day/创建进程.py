#要创建进程我们要导入multiprocessing模块
from multiprocessing import Process
import os
def run1(num,name):
    # while True:
    #     print('1')
    print(name)
    for i in range(0,num):
        print(i)
        #os.getpid():获取当前进程的id
        #os.getppid():获取当前进程的父进程id
        print('子进程pid'+str(os.getpid())+str(os.getppid()))
        #获取进程名称
        #Process.

if __name__ == '__main__':

    print('主进程的pid'+str(os.getpid()))
    
    #创建进程
    process1 = Process(target=run1,name='进程１号',args=(200,'子进程process1'))
    #启动进程
    process1.start()

    #判断进程是否存活
    # print('-------',process1.is_alive())

    #结束一个进程terminate
    process1.terminate()

    #添加一个join()方法
    process1.join()

    print('-------',process1.is_alive())

    for i in range(0,100):
        print('进程pid'+str(os.getpid()))

    print('主进程结束')