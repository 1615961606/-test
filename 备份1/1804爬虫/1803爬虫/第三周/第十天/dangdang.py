import requests
import re
from lxml import etree
import urllib.parse as parse
import pymysql
import json,time
class lagouspider(object):

    def __init__(self,conn):

        self.conn = conn
        #创建游标
        # self.cursor = conn.cursor()
        #创建游标
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    def crawl_data(self):
        url = 'http://category.dangdang.com/cp01.36.00.00.00.00.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36'

        }
        response = requests.get(url,headers=headers)
        #用gbk格式
        html = response.content.decode('gbk')
        html = etree.HTML(html)
        #获取所有的li标签
        list1 = html.xpath("//ul[@class='bigimg']//li//p[@class='name']/a[1]/@href")
        #获取详情
        detail = html.xpath("//ul[@class='bigimg']//li//p[@class='detail']/text()")
        #获取标题
        titile = html.xpath("//ul[@class='bigimg']//li//p[@class='name']/a[1]/@title")
        #便利所有的网址
        for i in list1:
            print(i)
            dict = {
                'contents':str(i)
            }
            # dict = parseurlencode(dict,encoding='utf8')
            self.write_data_to_db(dict)
            #请求头来反反爬虫
            headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36'
        }
            response2 = requests.get(i,headers=headers)
            html2 = response2.text
            print(html2)
            html2 = etree.HTML(html2)
            # title = html2.xpath("")
            # # print(html2)
            # print(title)
    def write_data_to_db(self,dict):
       
            into_sql = """
            INSERT INTO dangs(%s) VALUES(%s)
            """ % (','.join([key for key,value in dict.items()]),
            ','.join(['%s' for key,value in dict.items()])
            )
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
    mysql_conn = pymysql.Connect('localhost','root','bc123','tengxun',charset='utf8')
    spider = lagouspider(mysql_conn)
    spider.crawl_data()
    # spider.write_data_to_db(dict)        
            
if __name__ == '__main__':
    main()