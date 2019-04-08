# https://www.hao123.com/feedData/data?callback=jQuery18200711633952762396_1540541207297&type=ent&app_from=pc_tuijian&rn=10&page=3&_=1540541290434
# https://www.hao123.com/feedData/data?callback=jQuery18200711633952762396_1540541207287&type=rec&app_from=pc_tuijian&rn=10&page=2&_=1540541429869
# https://www.hao123.com/feedData/data?callback=jQuery18200711633952762396_1540541207287&type=military&app_from=pc_tuijian&rn=10&page=2&_=1540541647131
# https://tuijian.hao123.com/ent
import requests
from lxml import etree
import re
def hao123():
    url = 'https://tuijian.hao123.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    content = response.text
    html = etree.HTML(content)
    start_url = html.xpath('//ul[@class="clearfix"]/li')
    # print(start_url)
    for i in start_url:
        url = i.xpath('./a/@href')[0]+'\)'
        print(url)
        parrtrn = re.compile('tuijian.hao123.com\/(.*?)\\\\\)',re.S)
        result_url = re.findall(parrtrn,url)
        print(result_url)

if __name__ == '__main__':
    hao123()