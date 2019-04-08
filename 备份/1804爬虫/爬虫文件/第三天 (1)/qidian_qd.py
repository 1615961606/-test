#1.获取起点中文网的所有小说信息

# https://www.qidian.com/all?orderId=&style=1&pageSize=20
# &siteid=1&pubflag=0&hiddenField=0&page=1

# https://www.qidian.com/all?orderId=&style=1&pageSize=20
# &siteid=1&pubflag=0&hiddenField=0&page=2
from urllib import request,error
import re, pymysql

#创建数据库连接
# host=None, user=None, password="",
# database=None, port=3306,charset=''
mysql_conn = pymysql.Connect(
    '127.0.0.1','root','ljh1314','qd_class1804',port=3306,charset='utf8'
    )
#创建一个游标
cursor = mysql_conn.cursor()

def qidian_spider():
    
    #构建一个完整的url
    full_url = 'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page='+str(1)
    download_page_by_url(full_url)

def download_page_by_url(url):

    req_header = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }

    #构建一个Request对象
    req = request.Request(url,headers=req_header)
    
    try:
        #发起请求
        response = request.urlopen(req)
        if response.status == 200:
            htmldata = response.read().decode('utf-8')
            parse_page_data(htmldata)
            #提取下一页的链接地址
            pattern = re.compile(
                '<li.*?lbf-pagination-item"><a\shref="(.*?)".*?>.*?</a>.*?</li>',
                re.S
            )
            result = re.findall(pattern,htmldata)
            # print(result)
            # 获取下一页的连接
            next_url = result[1]
            if next_url is not 'javascript:;':
                next_url = 'https:'+next_url
                download_page_by_url(next_url)
                print('正在下载'+next_url)


            
    except error.HTTPError as err:
        print(err.reason)
    except error.URLError as err:
        print(err.reason)

    
def parse_page_data(html):
    #这里做数据的提取（采用正则提取）

    pattern = re.compile(
        '<div.*?book-img-box.*?<a.*?href="(.*?)"'+
        '.*?<div.*?book-mid-info.*?<a.*?>(.*?)</a>'+
        '.*?<a.*?name.*?>(.*?)</a>.*?<a.*?>(.*?)</a>'+
        '.*?<a.*?>(.*?)</a>.*?<p.*?intro">(.*?)</p>',
        re.S
    )
    novel_list = re.findall(pattern,html)
    print(len(novel_list))
    print(novel_list)
    for note in novel_list:
        note_dict = {}
        note_dict['image_url'] = note[0]
        note_dict['title'] = note[1]
        note_dict['author'] = note[2]
        note_dict['tag'] = note[3]+'|'+note[4]
        note_dict['content'] = note[5].replace('/r','').replace(' ','')
        insert_data_to_db(note_dict)


def insert_data_to_db(subdict):
    sql = """
    INSERT INTO qidian(%s)
    VALUES(%s)
    """ % (','.join(subdict.keys()),','.join(['%s']*len(subdict)))
    # print(sql)

    try:
        cursor.execute(sql,[value for key,value in subdict.items()])
        mysql_conn.commit()
    except Exception as err:
        print(err)
        mysql_conn.rollback()

    





if __name__ == '__main__':
    # startpage = 
    # endpage = 2
    # qidian_spider(startpage,endpage)
    qidian_spider()


