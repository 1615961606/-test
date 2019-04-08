import threading
import time

num = 0

#累加
def add_num(num1):
    global num
    for _ in range(0,num1):
        num+=1
        time.sleep(0.2)

def result():
    print(num)

if __name__ == '__main__':

    #创建线程
    td1 = threading.Thread(target=add_num,args=(100,))
    td2 = threading.Thread(target=result)

    #开启线程
    td1.start()
    td1.join()

    #添加等待时间的目的，为了等待线程td1中的任务只想完毕
    time.sleep(25)
    
    td2.start()
    td2.join()
    



    
