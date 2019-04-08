import requests
import re
from lxml import etree
import os
import pymysql
class lagouspider(object):

    def __init__(self,conn):

        self.conn = conn
        #创建游标
        # self.cursor = conn.cursor()
        #创建游标
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    def crawl_data(self):
        url = 'https://www.23us.so/list/4_1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

        }
        response = requests.get(url,headers=headers)
        content = response.content.decode()
        html = etree.HTML(content)
        # print(content)
        title = html.xpath("//td[1]/a/text()")
        # print(title)
        urls = []

        for i in title:
            # print(i)
            file_path = 'hehe1/'+i
            urls.append(i)
            # print(urls)
                #判断当前文件夹是否存在
            if not os.path.exists(file_path):
                    #如果不存在，则创建文件夹
                os.mkdir(file_path)
    
        ip = html.xpath("//td[1]/a/@href")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

        }
        
        for p in ip:
            response2 = requests.get(p,headers=headers)
            content2 = response2.content.decode()
            html2 = etree.HTML(content2)
            # print(content2)

            # print(ip)
        for t in urls:
            dict = {
                'contents':str(t)
            }
            self.write_data_to_db(dict)
            
            title2 = html2.xpath("//p[@class='pl']/b/text()")
            title3 = html2.xpath("//dd/p[2]/text()")
        

    def write_data_to_db(self,dict):
     
            into_sql = """
            INSERT INTO dings(%s) VALUES(%s)
            """ % (','.join([key for key,value in dict.items()]),
            ','.join(['%s' for key,value in dict.items()])
            )
                    # print(into_sql)
            print([value for key,value in dict.items()])

                    #执行插入的操作
            try:
                self.cursor.execute(into_sql,[value for key,value in dict.items()])
                        #提交
                self.conn.commit()
                print('插入成功')
            except:
                    #插入失败回滚
                print('插入失败')
                self.conn.rollback()            
def main():
 
    mysql_conn = pymysql.Connect('localhost','root','bc123','ding',charset='utf8')
    spider = lagouspider(mysql_conn)
    spider.crawl_data()
    # spider.write_data_to_db(dict)

if __name__ == '__main__':
    main()

