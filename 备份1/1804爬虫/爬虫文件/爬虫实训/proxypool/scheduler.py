#代理池
from crawlproxy import CrawlProxy
from manageip import ManageIp
from ckeckip import CheckIp
from multiprocessing import Process

class Scheduler(object):

    def __init__(self):
        self.manage_ip = ManageIp(database='proxydb',col_name='proxycol')

    def run_crawl_proxy(self):
        crawl_proxy = CrawlProxy(req_url='')
        # for _ in range(10):
        crawl_proxy.crawl_proxy_data()

    def run_check_proxy(self):
        check_proxy = CheckIp(test_url='https://www.baidu.com/')
        check_proxy.run()

    def run(self):
        #创建一个进程执行代理爬取
        process1 = Process(target=self.run_crawl_proxy)
        process1.start()
        #创建一个进程进行代理检测
        process2 = Process(target=self.run_check_proxy)
        process2.start()

if __name__ == '__main__':

    scheduler = Scheduler()
    scheduler.run()
        

    
