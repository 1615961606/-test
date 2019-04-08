#如何使用进程池
# from multiprocessing import Pool
# import requests

# def download_data_by_page(page,name):
#     print(page,name)
#     #http://blog.jobbole.com/all-posts/page/2/
#     full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
#     req_headers = {
#         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#     }

#     response = requests.get(full_url,headers=req_headers)
#     if response.status_code == 200:
#         print(response.text)
#         #可以在这里做数据解析


# if __name__ == '__main__':

#     #创建一个进程池
#     process_pool = Pool(4)

#     for page in range(0,1000):
#         #往进程池中添加任务
#         process_pool.apply_async(download_data_by_page,(1,'进程池'))
    
#     #关闭进程池，后面不能再添加任务了
#     process_pool.close()
#     #子进程先执行，执行完毕后，再继续执行主进程代码
#     process_pool.join()

#python自带的进程池模块
from concurrent.futures import ProcessPoolExecutor
import requests

def download_data_by_page(page,name):
    print(page,name)
    #http://blog.jobbole.com/all-posts/page/2/
    full_url = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    response = requests.get(full_url,headers=req_headers)
    if response.status_code == 200:
        print(response.status_code)
        #可以在这里做数据解析

        return response.text

#可以在回调函数中做数据解析
def download_done(future):
    print(future.result())

if __name__ == '__main__':
    
    #创建一个进程池
    pool = ProcessPoolExecutor(4)

    for page in range(0,100):
        handler = pool.submit(download_data_by_page,page,'下载任务')
        handler.add_done_callback(download_done)

    pool.shutdown()
    
python的多线程：
有一个全局解释器锁（GIL）：意味着python中的多线程其实是并发的操作

对比线程和进程
１．定义：
进程：是操作系统分配资源和调度的基本单元
线程:是依赖于进程执行，线程是cpu执行调度的最小单元

２．区别：
进程是会分配资源空间，每一个进程之间的资源不共享
线程不占用资源空间，线程之间的资源是共享的，为了防止资源错乱，我们一般加线程锁

３．使用场景：
进程一般情况下处理计算密集型任务
线程一般处理I/O密集型任务

