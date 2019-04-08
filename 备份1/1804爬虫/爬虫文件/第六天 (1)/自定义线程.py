import threading

#自定义线程
class customThread(threading.Thread):
    
    def __init__(self,threadname):
        super(customThread,self).__init__()
        self.threadname = threadname

    def run(self):
        print(self.threadname+'正在执行')
        for i in range(0,100):
            print(i)

if __name__ == '__main__':
    #创建线程
    cus_thread = customThread(threadname="自定义线程１号")
    #启动自定义的线程
    cus_thread.start()


