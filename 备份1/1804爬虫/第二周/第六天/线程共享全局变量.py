import threading
import time

num = 0

def add_num(num1):
    global num
    for i in range(1,num1):
        num+=1
        # time.sleep(0.01)

def result():
    print(num)

if __name__ == '__main__':
    td1 = threading.Thread(target=add_num,args=(101,))
    td2 = threading.Thread(target=result)


    td1.start()
    td1.join()
    time.sleep(3)
    td2.start()
    td2.join()
