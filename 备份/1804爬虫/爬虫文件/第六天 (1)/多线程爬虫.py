import threading,requests,queue,json
from lxml import etree

def download_page_data(teskQueue,dataQueue):
    #1.根据url发起请求（http://blog.jobbole.com/all-posts/page/4/）
    while teskQueue.empty() is not True:
        print(threading.current_thread().name+'正在下载数据')
        page = teskQueue.get()
        fullurl = 'http://blog.jobbole.com/all-posts/page/%s/' % str(page)
        #发起请求
        req_headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        response = requests.get(fullurl,headers=req_headers)
        if response.status_code == 200:
            print('数据加入成功')
            #2.将获取的响应结果，保存在数据队列里面
            dataQueue.put(response.text)

          
def parse_data(dataQueue,lock):
    #1.从数据队列中取出响应的结果
    #2.解析数据
    while dataQueue.empty() is not True:
        print(threading.current_thread().name+'正在解析')
        data = dataQueue.get()
        #构建一个xpath的解析器对象
        xp_data = etree.HTML(data)

        #提取数据：
        articles = xp_data.xpath('//div[@id="archive"]/div')
        print(len(articles))

        for article_div in articles:
            article_dict = {}
            #取标题
            titles = article_div.xpath('.//a[@class="archive-title"]/text()')
            if len(titles) > 0:
                article_dict['title'] = titles[0]
            else:
                article_dict['title'] = '未知'
            #简介
            desc = article_div.xpath('.//span[@class="excerpt"]/p/text()')
            if len(desc) > 0:
                article_dict['desc'] = desc[0]
            else:
                article_dict['desc'] = '暂无简介' 
            #日期
            article_dict['publishtime'] = ''.join(article_div.xpath('.//div[@class="post-meta"]/p/text()')).replace(' ','').replace('\r\n','')
            print(article_dict)

            #将获取的数据写入本地文件
            #加锁
            lock.acquire()
            with open('jobbole.json','a') as file:
                file.write(json.dumps(article_dict,ensure_ascii=False)+'\n')
            #解锁
            lock.release()

if __name__ == '__main__':
    
    #任务队列
    #maxsize:表示队列中允许存储的最大元素个数
    teskQueue = queue.Queue(maxsize=100)

    #存储url的页码
    for page in range(1,101):
        teskQueue.put(page)

    #数据队列
    dataQueue = queue.Queue()

    #创建一个线程锁
    lock = threading.Lock()

    #构造爬取线程
    crawl_threads = []
    crawl_thread_names = ['天宫１号','天宫2号',
                         '天宫3号','天宫4号']
    for crawl_name in crawl_thread_names:
        td = threading.Thread(target=download_page_data,args=(teskQueue,dataQueue),name=crawl_name)
        crawl_threads.append(td)
        #启动线程，执行任务
        td.start()
        # td.join()

    for thread in crawl_threads:
        #先执行下载线程的任务（子线程），执行完毕后，再执行主线程
        thread.join()

    #构造解析线程
    parse_threads = []
    parse_thread_names = ['蚕蛾1号','蚕蛾2号','蚕蛾3号','蚕蛾4号']
    for parse_name in parse_thread_names:
        #构造解析线程
        td = threading.Thread(target=parse_data,name=parse_name,args=(dataQueue,lock))
        parse_threads.append(td)
        #启动线程，执行任务
        td.start()

    for thread in parse_threads:
        thread.join()




