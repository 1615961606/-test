from bs4 import BeautifulSoup
import requests
import time as times
import pymysql
mysql_conn = pymysql.Connect('127.0.0.1','root','bc123','qidian_chen',port=3306,charset='utf8')
cursor = mysql_conn.cursor()
def che_spider(url):
    # print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content.decode('gbk'),features='html.parser')
    che_even = soup.find_all(name='ul',attrs={'class':'article'})

    print(len(che_even))
    for i in che_even:
        ul1 = i.find_all(name='li')
        for p in ul1:
            if p.select('a h3') == []:
                break
            title = p.select('a h3')[0].get_text()
            qc_url = p.select('a div.article-pic img')[0].attrs['src']
            time = p.select('a div.article-bar span.fn-left')[0].get_text()
            eyes = p.select('a div.article-bar span.fn-right em')[0].get_text()
            # comment = p.select('a div.article-bar span.fn-right em')[1].get_text
            qc_content = p.select('a p')[0].get_text()
          
            next_page = soup.select('.page-item-next')
            # print(next_page)
            dict = {
                'title':title,
                'qu_url':qc_url,
                'time':time,
                'eyes':eyes,
                'qc_content':qc_content
            }
            write_data_db(dict)
            if soup.select('.page-item-next') == []:
                print('ssadasf')
                che_spider('https://www.autohome.com.cn/all/11/#liststart')
            next_pages = soup.select('.page-item-next')[0].attrs['href']
                
            # print(next_pages)
            next_pagesx = 'https://www.autohome.com.cn/'+next_pages+'#liststart'
            che_spider(next_pagesx)

            if not next_page:
                print('sss')
                break
            break
def write_data_db(main_data):
    # print(main_data)
    sql = """
    INSERT INTO qiche(%s) VALUES(%s)
    """%(','.join(main_data.keys()),','.join(['%s']*len(main_data)))
    try:
        cursor.execute(sql,[value for key,value in main_data.items()])
        mysql_conn.commit()
        print('写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()

if __name__ == '__main__':
    url = 'https://www.autohome.com.cn/all/1/#liststart'

    che_spider(url)