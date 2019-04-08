from selenium import webdriver
from lxml import etree
import requests
import pymysql

mysql_conn = pymysql.Connect('127.0.0.1','root','bc123','qidian_chen',port=3306,charset='utf8')
cursor = mysql_conn.cursor()
opt = webdriver.ChromeOptions()
opt.set_headless()


def daxues():
    driver = webdriver.Chrome(options=opt, executable_path='/home/bc/桌面/chromedriver')
    driver.get('http://faculty.hust.edu.cn/pyjs.jsp?urltype=tsites.PinYinTeacherList&wbtreeid=1001&py=f&lang=zh_CN')
    html = driver.page_source
    htmls = etree.HTML(html)
    name = htmls.xpath('//ul[@class="pic-list clearfix"]/li/a/@href')

    for i in name:
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
        response = requests.get(i, headers=headers)
        html1 = response.content.decode()
        html2 = etree.HTML(html1)
        name = html2.xpath('//div[@class="js-top clearfix"]/div[@class="info"]/h2/text()')
        print(name)
        xinxi = ''.join(html2.xpath('//div[@class="blockwhite Psl-info"]/div[@class="cont"]/p/text()')).replace('\n','').replace('\xa0','').replace('\r','').replace(' ','')
        phone = ''.join(html2.xpath('//div[@class="blockwhite Ot-ctact"]/div[@class="cont"]//p/text()')).replace(' ','')
        fx = ''.join(html2.xpath('//div[@class="blockwhite Rsh-focus"]/div[@class="cont"]/ul/li/text()')).replace('\n','')
        dict = {
            'xinxi':xinxi,
            'phone':phone,
            'fx':fx,
            'name':name
        }
        print(dict)
        write_data_db(dict)
def write_data_db(main_data):
    # print(main_data)
    sql = """
    INSERT INTO xue(%s) VALUES(%s)
    """%(','.join(main_data.keys()),','.join(['%s']*len(main_data)))
    try:
        cursor.execute(sql,[value for key,value in main_data.items()])
        mysql_conn.commit()
        print('写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()
if __name__ == '__main__':
    daxues()