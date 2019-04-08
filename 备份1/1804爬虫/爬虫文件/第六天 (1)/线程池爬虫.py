from concurrent.futures import ThreadPoolExecutor
import requests

def download_page_data(page,):
    print('执行下载任务')
    print(page)

    fullurl = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
    #发起请求
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(fullurl,headers=req_headers)
    if response.status_code == 200:
        print('数据加入成功')
        #2.将获取到的页面源码数据，返回
        return response.text,response.status_code

def download_done(future):
    print(future.result)
    

if __name__ == '__main__':
    #实例化一个线程池
    #max_workers:在线程池中要创建的线程的数量
    thread_pool = ThreadPoolExecutor(max_workers=10)

    for page in range(1,101):
        handler = thread_pool.submit(download_page_data,page)
        handler.add_done_callback(download_done)

    thread_pool.shutdown() #->实际上调用了join()方法
    