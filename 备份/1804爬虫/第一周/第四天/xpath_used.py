#xpath的使用
from lxml import etree
import requests
import re

def maoyanspider(url):

    req_headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
      'Referer': 'http://maoyan.com/cinemas',
      'Cookie': 'uuid_n_v=v1; uuid=40F7CE30D2AC11E8ACF33DEFC63BA553F8D591A5CB6B42A2AC3DB92B6A5473AD; _csrf=620178448a83d981ded6119984dec00120f1cb915835031f1922ebf6d1bd2760; _lxsdk_cuid=16686333a62c8-05b029f5f19c5e-3a614f0b-144000-16686333a62c8; _lxsdk=40F7CE30D2AC11E8ACF33DEFC63BA553F8D591A5CB6B42A2AC3DB92B6A5473AD; ci=1; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=55292436.1539849797245.1539850388259.1539850391837.6; _lxsdk_s=16686333a62-f88-e9c-5b2%7C%7C15'
    }

    response = requests.get(url,headers=req_headers)

    # print(response.status_code)
    # print(response.text)
    if response.status_code == 200:
        xp_html = etree.HTML(response.text)
        # print(xp_html)
        result = xp_html.xpath('//div[@class="cinemas-list"]/div[@class="cinema-cell"]')
        # print(len(result))
        for i in result:
            title = i.xpath('./div[@class="cinema-info"]/a/text()')
            # print(title)
        #下一页如何提取这个链接：
        # pattern = re.compile('<li.*?<a\sclass="page_\d+.*?href="(.*?)".*?>.*?</a>.*?</li>',re.S)

        # result = re.findall(pattern,response.text)

        # print(result)
        next_url = xp_html.xpath('//ul[@class="list-pager"]/li[last()]/a/@href')[0]
        # print(next_url)
        if next_url is not 'javascript:void(0);':
            #构建了一个完整的url
            full_url = 'http://maoyan.com/cinemas' + next_url
            print(full_url)
            maoyanspider(full_url)

if __name__ == '__main__':

    url = 'http://maoyan.com/cinemas?offset=0'
    
    maoyanspider(url)
