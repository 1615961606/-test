#要创建进程，首先要导入multiprocessing这个模块
from multiprocessing import Process
import os
def run1(num,name):
    print(num,name)
    # while True:
    #     print('1')
    for i in range(0,num):
        print('子进程pid'+str(os.getpid()))
    print('主进程结束')

    
if __name__ == '__main__':
    print('主进程的id'+str(os.getpid())+str(os.getppid))
    #创建进程
    process1 = Process(target=run1,args=(200,'子进程'),name='进程一号')
    #启动进程
    process1.start()
    process1.join()
    print('========================================')
    print(process1.is_alive)

    # while True:
    #     print('2')
