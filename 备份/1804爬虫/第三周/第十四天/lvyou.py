import requests
from lxml import etree
import pymongo

def baidu():
    url = 'https://lvyou.baidu.com/scene/t-sheying/?rn=12&pn=24'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    content = response.content.decode()
    html = etree.HTML(content)
    detail_url = html.xpath('//h3[@class="fl"]/a/@href')
    for url in detail_url:
        urls = 'https://lvyou.baidu.com'+url 
    # print(detail_url)
        detail_page(urls)
def detail_page(urls):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response_detail = requests.get(urls,headers=headers)
    content_detail = response_detail.content.decode()
    html_content_detail = etree.HTML(content_detail)
    name = html_content_detail.xpath('//a[@class="clearfix"]/text()')[0]
    score = html_content_detail.xpath('//div[@class="main-score"]/text()')[1].replace('\n','')
    comments = html_content_detail.xpath('//a[@class="remark-count"]/text()')[0]
    desc = html_content_detail.xpath('//p[@class="main-desc-p"]/text()')[1].replace('\n','').replace(' ','')
    abstract = html_content_detail.xpath('//span[@class="main-besttime"]/span/text()')[0].replace('\n','').replace(' ','')
    comment_url = html_content_detail.xpath('//a[@class="remark-count"]/@href')
    you_dict = {
        'name':name,
        'score':score,
        'comments':comments,
        'desc':desc,
        'abstract':abstract,
        'comment_url':','.join(comment_url)
    }
    for url in comment_url:
        url_com = 'https://lvyou.baidu.com'+url
        comment_detail(url_com,you_dict)

def comment_detail(url_com,you_dict):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response_com = requests.get(url_com,headers=headers)
    content_com = response_com.content.decode()
    html_com = etree.HTML(content_com)
    name_com = html_com.xpath('//div[@class="ri-avatar-wrap"]/a[@class="ri-uname"]/@title')
    comment_content = html_com.xpath('//div[@class="ri-remarktxt"]/text()')
    comment_time = html_com.xpath('//div[@class="ri-time"]/text()')
    have_good = html_com.xpath('//a[@class="ri-dig ri-dig-available"]/span/text()')
    replay = html_com.xpath('//a[@class="ri-comment"]/span/text()')
    you_dict['name_com'] = ','.join(name_com)
    you_dict['comment_content'] =','.join(comment_content)
    you_dict['comment_time'] = ','.join(comment_time)
    you_dict['have_good'] = ','.join(have_good)
    you_dict['replay'] = ','.join(replay)
    insert_mongodb_data(you_dict)

def insert_mongodb_data(you_dict):
    print('正在存储')
    client = pymongo.MongoClient('127.0.0.1',27017)
    db = client['youdb']
    col = db['yous']
    col.insert(dict(you_dict))
    client.close()
if __name__ == '__main__':
    baidu()