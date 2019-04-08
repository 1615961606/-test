from lxml import etree
import requests
import pymysql

mysql_conn = pymysql.Connect('127.0.0.1','root','bc123','qidian_chen',port=3306,charset='utf8')
cursor = mysql_conn.cursor()
def qidian():
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入截止页码'))
    for i in range(start_page,end_page):
        qi_url = 'https://www.qidian.com/free/all?page='.format(i)
        get_page_data(qi_url)

def get_page_data(qi_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(qi_url)
    # print(response.text)
    html1 = response.text
    # print(html1)
    xp_html = etree.HTML(html1)
    all_li = xp_html.xpath('//ul[@class="all-img-list cf"]/li')
    # print(all_li)
    all_q_url = []
    for li in all_li:
        q_title = li.xpath('./div[@class="book-mid-info"]/h4/a/text()')[0]
        q_name = li.xpath('./div[@class="book-mid-info"]/p/a[1]/text()')[0]
        q_tags = li.xpath('./div[@class="book-mid-info"]/p/a[2]/text()')[0]+'·'+li.xpath('./div[@class="book-mid-info"]/p/a[3]/text()')[0]
        # q_tags1 = li.xpath('./div[@class="book-mid-info"]/p/a[3]/text()')[0]
        q_content = li.xpath('./div[@class="book-mid-info"]/p[2]/text()')[0]
        q_detail_url = li.xpath('./div[@class="book-mid-info"]/h4/a/@href')[0]
        # print(q_detail_url)
        
        all_q_url.append('https:'+q_detail_url+'#Catalog')
        zj_data = {
            'q_title':q_title,
            'q_name':q_name,
            'q_tags':q_tags,
            'q_content':q_content,
            'q_detail_url':q_detail_url
        }
        write_data_dbs(zj_data)
    qi_detail_url(all_q_url)

def qi_detail_url(all_q_url):
    all_zj_url = []

    for url_qi in all_q_url:
        # print(url_qi)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(url_qi,headers=headers)
        # print(response.text)
        xp_html1 = etree.HTML(response.text)
        all_li_data = xp_html1.xpath('//ul[@class="cf"]/li')
        # print(len(all_li_data))
        for zj in all_li_data:
            zj_title = zj.xpath('./a/text()')
            zj_url = zj.xpath('./a/@href[1]')
            # print(zj_url)
            # print(zj_title)
            zj_url = ','.join(zj_url)
            all_zj_url.append('https:'+str(zj_url)+'#Catalog')
            # print(all_zj_url)
           
        qi_detail_content(all_zj_url)
def qi_detail_content(all_zj_url):
    for url in all_zj_url:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
        print(len(url))

        response_detail = requests.get(url,headers=headers)
        # print(response_detail.text)
        many_data = etree.HTML(response_detail.text)
        detail_data = many_data.xpath('//div[@class="read-content j_readContent"]/p/text()')
        # print(detail_data) 
        detail_title = many_data.xpath('//h3[@class="j_chapterName"]/text()')
        print(detail_title)
        main_data = {
            'detail_title':','.join((detail_title)),
            'detail_data':','.join((detail_data)).replace('\n','').replace('\u3000','')
        }
        # print(main_data) 
        write_data_db(main_data)
def write_data_db(main_data):
    # print(main_data)
    sql = """
    INSERT INTO title_wz(%s) VALUES(%s)
    """%(','.join(main_data.keys()),','.join(['%s']*len(main_data)))
    try:
        cursor.execute(sql,[value for key,value in main_data.items()])
        mysql_conn.commit()
        print('写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()

def write_data_dbs(main_data):
    # print(main_data)
    sql = """
    INSERT INTO title_jj(%s) VALUES(%s)
    """%(','.join(main_data.keys()),','.join(['%s']*len(main_data)))
    try:
        cursor.execute(sql,[value for key,value in main_data.items()])
        mysql_conn.commit()
        print('简介写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()


def main():
        qidian()

if __name__ == '__main__':
    main()