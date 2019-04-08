#单线程执行
import time
import threading
def saysoory():
    for i in range(0,5):
        print('老婆对不起'+threading.current_thread().name)
        time.sleep(1)

def do():
    for i in range(0,5):
        print('捏捏腿'+threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    #同时执行两个任务
    #target:线程执行的目标函数
    #name:给线程起一个名称
    #args:为目标函数，传递参数，是一个元组
    td1 = threading.Thread(target=saysoory)
    print('主线程开始执行'+threading.current_thread().name)
    td2 = threading.Thread(target=do)
    td1.start()
    td2.start()
    td1.join()
    td2.join()
    print('主线程执行完毕'+threading.current_thread().name)

    
