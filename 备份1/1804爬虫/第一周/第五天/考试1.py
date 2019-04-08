
import requests
from lxml import etree
import pymysql
def dangdang():
    dd_url = 'http://book.dangdang.com/01.21.htm?ref=book-01-A'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    dd_response = requests.get(dd_url,headers=headers)
    content_dd = dd_response.content.decode('gbk')

    fenlei_dang(content_dd)
def fenlei_dang(content_dd):
    # print(content_dd)
    html_dd = etree.HTML(content_dd)
    # print(html_dd)
    xp_url = html_dd.xpath('//dl[@class="primary_dl"]/dt//a[1]/@href')
    xp_title = html_dd.xpath('//dl[@class="primary_dl"]/dt//a/text()')
    # xp_urls = 'http://category.dangdang.com/cp01.21.02.00.00.00.html'
    for ii in xp_url:
        print(ii)
        get_data(ii)

def get_data(dd_url):
    print(dd_url)
    # for url in dd_url:
    #     print(url)
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
    detail_response = requests.get(dd_url,headers=headers)
    xp_html1 = etree.HTML(detail_response.content.decode('gbk'))
        

    all_detail_li = xp_html1.xpath('//ul[@class="bigimg"]/li')
   
    print(len(all_detail_li))
    for li in all_detail_li:
      
        # print()
        # image_url = li.xpath('./a//img')
        # de_title = li.xpath('./p[@class="name"]/a/text()')
        # price_dd = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')[0]
        # price_dj = li.xpath('./p[@class="price"]/a[@class="search_discount"]/text()')[0]
        # price_dj2 = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()')[0]
        # price_dj3 = li.xpath('./p[@class="price"]/span[@class="search_discount"]/text()')[0]
        # print(price_dj+price_dj2+price_dj3)
        comment_dd = li.xpath('//p[@class="search_star_line"]/a/text()')
        content_ddd = li.xpath('//p[@class="detail"]/text()')
        # print(price_dd)
        next_urls = xp_html1.xpath('//li[@class="next none"]/a/text()')
        next_url = xp_html1.xpath('//li[@class="next"]/a/@href')
        # if not next_url:
        #     print('爬取完毕')
        #     break

        # if ','.join(next_urls) != '下一页':
        #     print(','.join(next_urls))
        #     # break
        full_url = 'http://category.dangdang.com'+','.join(next_url)
        #     print(full_url)
        get_data(full_url)
        if ','.join(next_urls) == '下一页':
            print('1111111')
            break
            # dangdang()
        break
if __name__ == '__main__':
    # http://category.dangdang.com
# http://category.dangdang.com/pg2-cp01.21.02.00.00.00.html
# http://category.dangdang.com/pg2-cp01.21.15.00.00.00.html
    dangdang()