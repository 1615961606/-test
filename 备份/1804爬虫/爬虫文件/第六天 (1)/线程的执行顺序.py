import threading
import time

def do():
    print('我要唱歌'+threading.current_thread().name)
    time.sleep(1)

def danck():
    print('我要跳舞'+threading.current_thread().name)
    time.sleep(1)


if __name__ == '__main__':
    
    threads = []
    for _ in range(0,20):
        #创建线程
        td1 = threading.Thread(target=do)
        threads.append(td1)
        td2 = threading.Thread(target=danck)
        threads.append(td2)
    
    
    for thread in threads:
        #开启线程
        thread.start()
　　
    #结论
    #多线程的执行是没有顺序的

        


    