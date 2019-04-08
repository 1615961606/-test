import threading,requests,queue
from lxml import etree

def down_page_data(tesk,data):
    #将获取的数据队列
    while teskQueue.empty() is not True:
        print(threading.Thread().name+'正在下载数据')
        page = teskQueue.get()
        fullurl = 'http://blog.jobbole.com/all-posts/page/%s/'%str(page)
        #发起请求
        req_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(fullurl,headers=req_headers)
        if response.status_code == 200:
            print('数据加入成功')
            dataqueue.put(response.text)

def parse_data(dataQueue,locks):
    #取出相应结果
    while dataQueue.empty() is not True:
        data = dataQueue.get()
        xp_data = etree.HTML(data)

        article = xp_data.xpath('//div[@id="archive"]/div')

        for article_div in article:
            article_dict = {}
            article_dict['title'] = article_div.xpath('.//a[@class="archive-title"]/text()')
            article_dict['desc'] = article_div.xpath('.//span[@class="excerpt"]')
            article_dict['da_time'] = article_div.xpath('.//div[@class="post-meta"]/p/text()')
            print(article_dict)

            #将获取的数据写到本地
            # locks.acquire
if __name__ == '__main__':
    
    #任务队列
    # maxsize:表示队列中允许存储的最大元素个数
    teskQueue = queue.Queue(maxsize=100)

    #存储url页码
    for page in range(1,101):
        teskQueue.put(page)

    #数据队列
    dataqueue = queue.Queue()


    #创建一个线程锁
    lock = threading.Lock()
    #构造爬取线程
    crawl_threads = []
    crawl_thread_names = ['天宫一号','天宫二号','天宫三号','天宫四号']
    for crawl_name in crawl_thread_names:
        td = threading.Thread(target=down_page_data,args=(teskQueue,dataqueue),name=crawl_name)
        crawl_threads.append(td)
        #启动线程
        td.start()

    for thread in crawl_threads:
        thread.join() 

    #构造解析线程
    parse_threads = []
    parse_thread_names = ['嫦娥一号','嫦娥二号','嫦娥三号','嫦娥四号']
    for parse_name in parse_thread_names:
        #构造解析线程
        td = threading.Thread(target=parse_data,name=parse_name,args=(dataqueue,))
        parse_threads.append(td)
        td.start()