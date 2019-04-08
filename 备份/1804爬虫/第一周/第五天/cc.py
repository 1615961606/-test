import requests
from lxml import etree

url = 'http://category.dangdang.com/pg100-cp01.21.02.00.00.00.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = requests.get(url,headers=headers)
html = etree.HTML(response.text)
content = html.xpath('//li[@class="next none"]/a/text()')
print(','.join(content))