import re
import requests
from lxml import etree
url = 'http://www.quanshuwang.com/book/164/164263'
headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
            }
response = requests.get(url,headers=headers)
content = response.content.decode('gbk')
html = etree.HTML(content)
parrern = re.compile('<li>.*?<a.*?.*?href="(.*?)"',re.S)
# result = re.findall(parrern,content)
result = html.xpath('//div[@class="clearfix dirconone"]/li/a/@href')
print(result)
# print(content)