# file = "/home/bc/桌面/1803爬虫/第二周/第六天/os/ll.txt"
import os
import requests
import json
from lxml import etree
url = 'https://www.readnovel.com/rank/hotsales?pageNum=2'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
response = requests.get(url,headers=headers)
html = response.content.decode()
html = etree.HTML(html)
li_list = html.xpath("//div[@class='book-img-text']/ul/li")
# print(li_list)
for i in li_list:
    herf = i.xpath("./div[@class='book-img-box']/a/@href")
    title = i.xpath("./div[@class='book-mid-info']/h4/a/text()")
    # image = i.xpath(".//p[@class='author']/img/@src")
    image = "https:"+i.xpath("./div[@class='book-img-box']/a/img/@src")
    pp = i.xpath(".//p[@class='intro']/text()")
    print(image)

responses = requests.get(image,headers=headers)
with open('yy.jpg','wb+') as f:
    f.write(responses.content)
# file = os.mkdir("/home/bc/桌面/1803爬虫/第二周/第六天/%s"%'ka')

# with open('../第六天/ka/l.txt','w') as f:
#     f.write('hello,word')
