import urllib.request as request
import urllib.parse as parse
import ssl
import re
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

        startpage = int(input('请输入起始页'))
        endpage = int(input('请输入结束页'))
        for i in range(startpage,endpage+1):
            
            url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start={}#a'.format(i)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

            }
            ssl_context = ssl._create_unverified_context()
            req = request.Request(url,headers=headers)
            response = request.urlopen(req,context=ssl_context)
            content = response.read().decode()
            # content = json.loads(response.read().decode())

            # print(content)
            # parrern = re.compile('<td.*?l square.*?<a.*?href="(.*?)">',re.S)
            parrern = re.compile('<td.*?l square.*?<a.*?href="(.*?)">(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>')

            contentss = re.findall(parrern,content)
            str(contentss)
            # print(result)
            dict = {
                    'contents':str(contentss[0]),
                  

                }
            # dict = parseurlencode(dict,encoding='utf8')
            self.write_data_to_db(dict)
            # print(dict)
            

    def write_data_to_db(self,dict):
    # print(dict)
                #写入文件
                # with open('lagouinfo.txt','a+') as file:
                #     file.write(str(dict)+'\n')

                #写入数据库
        into_sql = """
        INSERT INTO tx(%s) VALUES(%s)
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
    # city = input('请输入城市名:')
    # startpage = int(input('起始页：'))
    # endpage = int(input('截止页：'))
    # kd = input('输入职位：')
    #创建mysql客户端连接
    mysql_conn = pymysql.Connect('localhost','root','bc123','tengxun',charset='utf8')
    spider = lagouspider(mysql_conn)
    spider.crawl_data()
    # spider.write_data_to_db(dict)

if __name__ == '__main__':
    main()