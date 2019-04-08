import requests
import re
import json
import pymysql
class lagouspider(object):

    def __init__(self,conn):

        self.conn = conn
        #创建游标
        # self.cursor = conn.cursor()
        #创建游标
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    def crawl_data(self):
        url = 'http://www.xicidaili.com/nn/2'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

        }
        response = requests.get(url,headers=headers)
        content = response.content.decode()
        # print(content)
        # ip_parttern = re.compile('<tr.*?country.*?<td>(.*?)</td>',re.S)
        # port_parttern = re.compile('<tr.*?country.*?<td.*?<td>(.*?)</td>',re.S)
        # adr_parttern = re.compile('<tr.*?country.*?<td.*?<td.*?<a.*?>(.*?)</a>',re.S)
        # time_parttern = re.compile('<tr.*?country.*?<td.*?<td.*?<td.*?bar.*?<td.*?<td>(.*?)</td>',re.S)
        # datatime_parttern = re.compile('<tr.*?country.*?<td.*?<td.*?<td.*?bar.*?<td.*?<td.*?<td>(.*?)</td>',re.S)

        # ip_result =  re.findall(ip_parttern,content)
        # port_results = re.findall(port_parttern,content)
        # adr_results = re.findall(adr_parttern,content)
        # time_results = re.findall(time_parttern,content)
        # data_time_results = re.findall(datatime_parttern,content)
        parrtern = re.compile('<tr.*?country.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<a.*?>(.*?)</a>.*?bar.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
        result = re.findall(parrtern,content)
        for i in result:
            ip = i[0],
            port = i[1],
            adress = i[2],
            time = i[3],
            yanz = i[4]
            # print(port)
            dict = {
                'ip':ip,
                'port':port,
                'adress':adress,
                'time':time,
                'yanz':yanz
    }
            self.write_data_to_db(dict)
    # with open('daili.json','a') as f:
    #     f.write(json.dumps(dict,ensure_ascii=False)+'\n')
# dict = {
#     'ip_result':ip_result,
#     'port_results':port_results,
#     'adr_results':adr_results,
#     'time_results':time_results,
#     'data_time_results':data_time_results

# }
# for key,value in dict.items():

#     with open('xi.json','a') as f:
#         f.write(json.dumps(str(key)+':'+str(value),ensure_ascii=False)+'\n')
# print(data_time_results)
# for key,value in dict.items():
#     print(key,value[0:5])
# print(dict)
# print(result)
    def write_data_to_db(self,dict):
        # print(dict)
                    #写入文件
                    # with open('lagouinfo.txt','a+') as file:
                    #     file.write(str(dict)+'\n')

                    #写入数据库
            into_sql = """
            INSERT INTO daili(%s) VALUES(%s)
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
    mysql_conn = pymysql.Connect('localhost','root','bc123','xici',charset='utf8')
    spider = lagouspider(mysql_conn)
    spider.crawl_data()
    # spider.write_data_to_db(dict)

if __name__ == '__main__':
    main()