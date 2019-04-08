# -*- coding:utf-8 -*-
import pymysql
import random
import re,time
import requests
from requests.exceptions import ProxyError,ConnectionError,SSLError,ReadTimeout,ConnectTimeout

test_url = 'https://www.baidu.com/'
timeout = 10

class RandomIpHandler:
    #初始化构造函数
    def __init__(self):
        self.client = pymysql.Connect('localhost','root','wgz123','ipproxy',3306)
        self.cursor = self.client.cursor(cursor=pymysql.cursors.DictCursor)
    
    def get_random_ip(self):
        #查询数据库中的所有数据
        select_SQL= 'select * from proxies'
        self.cursor.execute(select_SQL)
        #返回一个结果列表
        results=self.cursor.fetchall()
        #从中随机获取一个Ip
        result=random.choice(results)
        status,time = self.ipCheck(result)
        if status == True:
            print(result)
            #该代理可用，返回结果
            return result
        else:
            #如果获取的ip不可用，继续获取，直到可用为止
            self.get_random_ip()
            # 优化在这里我们可以做一个优化处理判断当前选取的ip是否可以使用
            # 优化点：如果判断当前的代理不可用，那么我们是否可以将数据库里面的这条数据删除掉？（自己实现）

    def ipCheck(self, ip_item):
        """代理检测"""
        proxy = ip_item['ip'] + ':'+ip_item['port']
        try:
            proxies = {
                'https': proxy
            }
            start_time = time.time()
            response = requests.get(test_url, timeout=timeout, proxies=proxies)
            if response.status_code == requests.codes.ok:
                end_time = time.time()
                used_time = end_time - start_time
                print('Proxy Valid'+proxy, 'Used Time:', used_time)
                return True, used_time
        #出现异常则代理不可用
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            print('Proxy Invalid:', proxy)
            return False, None


def main():
    handler = RandomIpHandler()
    ip = handler.get_random_ip()
    print(ip)

#入口函数
if __name__ == '__main__':
    main()




