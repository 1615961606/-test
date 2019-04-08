import threading
from concurrent.futures import ThreadPoolExecutor

def down_load(page,name):
    print(page,name)
    #根据page构建url,发起请求

    return '下载完成'
def done(future):
    print(future.result())


if __name__ == '__main__':
    print('主线程开始执行'+threading.Thread().name)
    pool = ThreadPoolExecutor(10)
    for page in range(1,51):
        handel = pool.submit(down_load,page,'class123')
        handel.add_done_callback(done)

    pool.shutdown()
    print('主线程执行完毕'+threading.Thread().name)
