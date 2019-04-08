import re
import json
import requests
from lxml import etree

def quan():
    for i in range(1,3):
        # url = 'http://www.quanshuwang.com/list/{}_1.html'.format(i)
        url = 'http://www.quanshuwang.com/list/1_1.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        content1 = response.content.decode('gbk')
        parrern = re.compile('<li.*?<img.*?>.*?href="(.*?)".*?>',re.S)
        result = re.findall(parrern,content1)
        # print(content1)

        for page in result:
            # print(i)
            # print(type(i))
        # print(content1)
            url2 = page
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
            }
            response2 = requests.get(str(url2),headers=headers)
            content2 = response2.content.decode('gbk')
            # parrern2 = re.compile('b-info.*?<h1>(.*?)</h1>',re.S)
            parrern2 = re.compile('b-oper.*?href="(.*?)"',re.S)
            result2 = re.findall(parrern2,content2)

            for p in result2:
                url3 = p
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
            }
                response3 = requests.get(url3,headers=headers)
                content3 = response3.content.decode('gbk')
                # print(content3)
                # print(url3)
                parrern3 = re.compile('clearfix dirconone.*?href="(.*?)"',re.S)
                result3 = re.findall(parrern3,content3)
                print(result3)
            # print(result2)
quan()