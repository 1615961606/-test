#单线程执行
import time

def saysorry():
    for i in range(0,5):
        print('老婆，对不起，我错了')
        time.sleep(1)

def do():
    for i in range(0,5):
        print('捏捏肩膀')
        time.sleep(1)



if __name__ == '__main__':
    saysorry()
    do()