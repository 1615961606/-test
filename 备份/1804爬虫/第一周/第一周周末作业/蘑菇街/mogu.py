import requests
from lxml import etree
import json
import re
import csv

all_tags = []

with open("mos.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)
please_enter = input('请您输入要搜索的关键字')

sorry = '对不起没有该分类'
def mogujie():
    url = 'https://mce.mogucdn.com/jsonp/multiget/3?callback=jQuery2110774644143548473_1540037697478&pids=109499%2C109520%2C109731%2C109753%2C110549%2C109779%2C110548%2C110547%2C109757%2C109793%2C109795%2C110563%2C110546%2C110544&appPlat=p&_=1540037697482'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers=headers)

    content = response.text
    
    parrern = re.compile('jQuery2110774644143548473_1540037697478\((.*?)\)')
    content1 = re.findall(parrern,content)
    contents = json.loads(content1[0])
    datas = contents['data']
    for gu in datas:
        mogu = datas[gu]['list']

        for all_gu in mogu:
            all_tags.append(all_gu['title'])
            m_title = all_gu['title']
            m_url = 'https:'+all_gu['link']
            dict = {
                m_title:m_url
            }
            dict_data(dict)


def dict_data(dict):
    for key,value in dict.items():

        if key == please_enter:
            result = value
            get_data(result)

def get_data(data_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    parrern = re.compile('https.*?book\/.*?\/(.*?)\?acm.*?',re.S)

    result1 = re.findall(parrern,data_url)
    data_urls = 'https://list.mogujie.com/search?callback=jQuery2110976958126674375_1540111580514&_version=8193&ratio=3%3A4&cKey=15&page=1&sort=pop&ad=0&fcid={}&action=boyfriend&acm=3.mce.1_10_1heto.109779.0.azme9r76dG3Cu.pos_3-m_406154-sd_119&_=1540111580515'.format(','.join(result1))


    content = requests.get(data_urls,headers=headers)
    html = content.text
    parrern_html = re.compile('jQuery.*?\((.*?)\)')
    result1_html = re.findall(parrern_html,html)
    # print(result1_html)
    z_html = json.loads(','.join(result1_html))
    result2 = z_html['result']['wall']['docs']

    for page in result2:
        sp_title = page.get('title')
        sp_img_url = page.get('img')
        sp_orgPrice = page.get('orgPrice')
        sp_price = page.get('orgPrice')
        sp_sale = page.get('sale')
        mogu_dict = {
        'title':sp_title,
        'imgurl':sp_img_url,
        'orgPrice':sp_orgPrice,
        'price':sp_price,
        'sale':sp_sale
    }
        print('------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------')
 
        print(mogu_dict)
    print('以上为所有搜索内容')

    



def main():

    mogujie()

if __name__ == '__main__':

    main()
