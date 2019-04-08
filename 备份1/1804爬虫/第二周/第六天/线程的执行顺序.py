import threading
import time

def do():
    print('我喜欢你'+threading.current_thread().name)
    time.sleep(1)

def dance():
    print('我要洗澡'+threading.current_thread().name)
    time.sleep(1)
threads = []
if __name__ == '__main__':
    for i in range(0,100):
        td1 = threading.Thread(target=do)
        threads.append(td1)
        td2 = threading.Thread(target=dance)
        threads.append(td2)

    for thread in threads:
        thread.start()