

        
#1.寻找目标ｕｒｌ,分析目标url
#目标url:https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false
# 参数由两部分组成：
# １．query string:
# city: 北京
# needAddtionalResult: false

# 2.form data:
# first: false
# pn: 2
# kd: java

import urllib.request as request
import urllib.parse as parse
import json,time
import pymysql

class lagouspider(object):

    def __init__(self,conn,city,kd,startpage,endpage):

        self.conn = conn
        #创建游标
        # self.cursor = conn.cursor()
        #创建游标
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.city = city
        self.kd = kd
        self.startpage = startpage
        self.endpage = endpage

    def crawl_data(self):

        query_data = {
            'city':self.city,
            'needAddtionalResult':'false'
        }
        #将参数转为url编码格式
        query_data = parse.urlencode(query_data)

        url = 'https://www.lagou.com/jobs/positionAjax.json?'+query_data

        #构造表单数据
        form_data = {
            'first':'false',
            'pn':1,
            'kd':self.kd
        }


        #构造请求头，不然会报错{"success":false,"msg":"您操作太频繁,请稍后再访问","clientIp":"61.148.245.94"}
        req_headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Referer':'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=',
        }

        for page in range(self.startpage,self.endpage+1):

            form_data['pn'] = page
            print(form_data)
            #2步转换,先将变淡数据转换为url编码格式，然后在将数据转为bytes数据
            url_form_data = parse.urlencode(form_data).encode('utf-8')
            print(url_form_data)

            #构造request请求对象
            req = request.Request(url,data=url_form_data,method="POST",headers=req_headers)

            #发起请求，获取响应
            response = request.urlopen(req)

            #打印结果
            # print(response.status)
            # print(response.read().decode())

            if response.status == 200:
                # 使用json模块下的loads()方法将json字符串,转换为ｐｙｔｈｏｎ对象．
                data = json.loads(response.read().decode())
                print(data)
                #获取当前页面的职位列表
                positions = data['content']['positionResult']['result']

                for position in positions:
                    # print(position)
                    #公司名称
                    compamy_name = position['companyShortName']
                    #职位标题
                    position_title = position['positionName']
                    #福利待遇
                    other = position['positionAdvantage']
                    #其他福利
                    companyLabelList = ','.join(position['companyLabelList'])
                    # .....自己写

                    dict = {
                        'compamy_name':compamy_name,
                        'position_title':position_title,
                        'other':other,
                        'companyLabelList':companyLabelList,
                    }

                    self.write_data_to_db(dict)
            
            if page == self.endpage:
                self.close()

    def write_data_to_db(self,dict):
        # print(dict)
        #写入文件
        # with open('lagouinfo.txt','a+') as file:
        #     file.write(str(dict)+'\n')

        #写入数据库
        into_sql = """
        INSERT INTO lagouinfo(%s) VALUES(%s)
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

    def read_data_from_db(self):
       #自己先实现，查找
       sql = '''
       SELECT * FROM lagouinfo
       '''
       result = self.cursor.execute(sql)
       #　result　返回收影响的行（只会返回行数）
       print(result)

       #获取一条查询结果
       data = self.cursor.fetchone()
       print(data)

       #获取所有的结果集
       data = self.cursor.fetchall()
       print(data)
    
    def close(self):
        self.read_data_from_db()
        print('关闭')
        #关闭数据库和游标
        self.cursor.close()
        self.conn.close()

def main():
    # city = input('请输入城市名:')
    # startpage = int(input('起始页：'))
    # endpage = int(input('截止页：'))
    # kd = input('输入职位：')
    #创建mysql客户端连接
    mysql_conn = pymysql.Connect('localhost','root','bc123','lagou',charset='utf8')
    spider = lagouspider(mysql_conn,'北京','java',1,2)
    spider.crawl_data()


if __name__ == '__main__':
    main()
