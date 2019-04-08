#单线程执行
import time
import threading
def saysoory():
    for i in range(0,5):
        print('老婆对不起')
        time.sleep(1)

def do():
    for i in range(0,5):
        print('捏捏腿')
        time.sleep(1)

if __name__ == '__main__':
    saysoory()
    do()