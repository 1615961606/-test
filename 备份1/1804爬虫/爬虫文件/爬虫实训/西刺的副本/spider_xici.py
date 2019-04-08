# -*- coding:UTF-8 -*-
import pymysql
from urllib.request import Request,urlopen
import re,time
import requests
from requests.exceptions import ProxyError,ConnectionError,SSLError,ReadTimeout,ConnectTimeout

test_url = 'https://www.baidu.com/'
timeout = 10

# 目标url的地址规律：
# http://www.xicidaili.com/nn/1
# http://www.xicidaili.com/nn/2
# http://www.xicidaili.com/nn/3

class Spider_IP:
    def __init__(self):
        self.client = pymysql.Connect('localhost','root','wgz123','ipproxy',3306)
        self.cursor = self.client.cursor()

    def get_ip_data(self,endpage):
        for i in range(1,endpage+1):
            print('正在获取第'+str(i)+'页')
            url = 'http://www.xicidaili.com/nn/'+ str(i)
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
            }
            #方式１
            # #构建一个request请求对象(url、data、headers)
            # req = Request(url,headers=headers)
            # #发起请求(可以)
            # response = urlopen(req)
            # #获取html源码
            # html = response.read().decode('UTF-8')
            # print(html)

            #方式2
            #发起请求(可以),获取响应
            response = requests.get(url,headers=headers)
            # #获取html源码
            html = response.text
            # html = response.content.decode('UTF-8')
            #编辑匹配的规则
            re_compile1 = re.compile(r'<tr.*?class="odd".*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?country.*?<td>(.*?)</td>.*?',re.S)
            result1 = re.findall(re_compile1,html)
            re_compile2 = re.compile('<tr.*?class="".*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?country.*?<td>(.*?)</td>.*?',re.S)
            result2 = re.findall(re_compile2,html)
            ip_result = result1+result2
            #返回所有的IP结果
            # return ip_result
            for ip_item in ip_result:
                print(ip_item)
                #只获取协议为HTTPS的代理
                if ip_item[2] == 'HTTPS':
                    #将获取的所有HTTPS协议类型的并且是高匿ip，存放进数据库
                    self.save_all_ip_todb(ip_item)
                    #检测代理是否可用
                    status,result = self.ipCheck(ip_item)
                    #返回结果为True代表可用
                    if status == True:
                        #将可用ip存放进数据库
                        self.save_used_ip_todb(ip_item)


    def ipCheck(self,ip_item):
        """代理检测"""
        proxy = ip_item[0] + ':'+ip_item[1]
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


    def save_used_ip_todb(self,ipitem):
        print(ipitem)
        print('正在保存可用代理'+ipitem[0])
        #构建数据库插入语句
        insert_sql = """
        INSERT INTO proxies(ip,port,type) VALUES(%s,%s,%s)
        """
        self.cursor.execute(insert_sql,ipitem)
        self.client.commit()

    def save_all_ip_todb(self,ipitem):
        # print(ipitem)
        print('正在保存代理'+ipitem[0])
        #构建数据库插入语句
        insert_sql = """
        INSERT INTO allproxies(ip,port,type) VALUES(%s,%s,%s)
        """
        self.cursor.execute(insert_sql,ipitem)
        self.client.commit()
    

if __name__ == '__main__':
    spider = Spider_IP()
    endpage = input('请输入截止页码：') 
    spider.get_ip_data(int(endpage)) 
    
    





