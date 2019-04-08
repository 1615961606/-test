from multiprocessing import Process
import time,queue
# data_list = []
queue = queue.Queue(200)

def write_data():
    for i in range(0,200):
        global queue
        queue.put(i)

    print(queue.full())

def get_data():
    print('-----')
    # time.sleep(10)
    global queue
    while queue.empty() is not True:
        print(queue.get())

if __name__ == '__main__':

    process1 = Process(target=write_data)
    process1.start()
    process1.join()

    process2 = Process(target=get_data)
    process2.start()
