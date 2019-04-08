import urllib.request as request
import urllib.parse as parse
import ssl
import re
import json
context = ssl._create_default_https_context()
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
}
from_data = {
    'first': 'false',
    'pn': '1',
    'kd': 'java',
}
from_data = parse.urlencode(query=from_data,encoding='utf-8')
req = request.Request(url,headers=headers,data=from_data)
response = request.urlopen(req,context=context)
print(response.status)
html = response.read().decode()
# html = json.dumps(html)
# pattern = re.compile('<li.*?position_link.*?>.*?>(.*?)</h3>',re.S)
# result = re.findall(pattern,html)

# print(result)
print(html)
# with open('lagou.json','a') as f:
#     f.write(json.dumps(dict,ensure_ascii=False)+'\n')