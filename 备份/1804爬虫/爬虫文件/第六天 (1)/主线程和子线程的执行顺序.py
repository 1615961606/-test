import threading
import time

def saysorry(num):
    for i in range(0,num):
        print('老婆，对不起，我错了'+threading.current_thread().name)
        time.sleep(1)

def do(num):
    for i in range(0,num):
        print('捏捏肩膀'+threading.current_thread().name)
        time.sleep(1)

if __name__ == '__main__':
    #同时执行两个任务
    #target:线程执行的目标函数
    #name:给线程起一个名称
    #args:为目标函数，传递参数，是一个元组
    print('主线程开始执行'+threading.current_thread().name)
    
    td1 = threading.Thread(target=saysorry,name='线程１号',args=(3,))
    td2 = threading.Thread(target=do,name='线程２号',args=(5,))
 
    #起动线程
    td1.start()
    td2.start()

　　 #先执行子线程里面的任务，当执行完毕后，再回到主线程中继续执行
    td1.join()
    td2.join()

    print('主线程执行完毕')