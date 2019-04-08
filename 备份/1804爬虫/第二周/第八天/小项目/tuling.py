from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import threading
import requests
from lxml import etree
import pymysql
#用进程池下载数据
pool = ProcessPoolExecutor(4)

mysql_conn = pymysql.Connect('127.0.0.1','root','bc123','tengxun',port=3306,charset='utf8')
cursor = mysql_conn.cursor()
def tulin(page):
    # for page in range(1,60):
    url = 'http://www.ituring.com.cn/book?tab=book&sort=hot&page={}'.format(str(page))
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
    response = requests.get(url,headers=headers)
    content = response.text
    html = etree.HTML(content)
    x_url = html.xpath('//div[@class="book-info"]/h4/a/@href')
    get_datail(x_url)

def get_datail(x_url):
    for url in  x_url:
        url = 'http://www.ituring.com.cn'+url
        # print(url)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
        response1 = requests.get(url,headers=headers)
        t_content = response1.text
        html1 = etree.HTML(t_content)


        img_url = html1.xpath('//div[@class="book-img"]/a/img/@src')
        
        title = html1.xpath('//div[@class="book-title"]/h2/text()')[0].replace(' ','').replace('\n','')
        author = html1.xpath('//div[@class="book-author"]/span/text()')[0].replace(' ','').replace('\n','').replace('\r','')
        yi_zhe = html1.xpath('//div[@class="book-author"]/span[2]/a/text()')
        if yi_zhe == []:
            yi_zhe ='未知'
        status = html1.xpath('//div[@class="book-status"]/span/text()')[0].replace(' ','').replace('\n','').replace('\r','')
        tags1 = html1.xpath('//span[@class="tags"]/a[1]/text()')
        tags2 = html1.xpath('//span[@class="tags"]/a[2]/text()')
        if tags2 ==[]:
            tags2 = '空'
        desc = html1.xpath('//div[@class="alert alert-warning"]/text()')
        if desc == []:
            desc ='空'
        desc2 = html1.xpath('//div[@class="book-intro readmore"]/text()')[0].replace(' ','').replace('\n','').replace('\r','')
        tuijian = html1.xpath('//a[@id="toggle-vote"]/span[1]/text()')[0]
        reads = html1.xpath('//div[@class="item article-vote"]/span[1]/text()')[0].replace(' ','').replace('\n','').replace('\r','')
        tese = html1.xpath('//div[@class="intro"]/text()')[0].replace(' ','').replace('\n','').replace('\r','')

        dict = {
            'img_url':','.join(img_url),
            'title':title,
            'author':author,
            'yi_zhe':','.join(yi_zhe),
            'status':status,
            'tags1':','.join(tags1),
            'tags2':','.join(tags2),
            'desc1':','.join(desc),
            'desc2':desc2,
            'tuijian':tuijian,
            'read1':reads,
            'tese':tese
        }
        # print(dict)
        write_data_db(dict)
def write_data_db(dict):
    sql = """
    INSERT INTO tls(%s) VALUES(%s)
    """%(','.join(dict.keys()),','.join(['%s']*len(dict)))
    try:
        cursor.execute(sql,[value for key,value in dict.items()])
        mysql_conn.commit()
        print('写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()
if __name__ == '__main__':
    # tulin()
    for page in range(1,60):
        handle = pool.submit(tulin,page)