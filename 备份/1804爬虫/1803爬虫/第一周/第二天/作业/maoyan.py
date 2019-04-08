import urllib.request as request
import ssl
import urllib.parse as parse
import json
import re
for i in range(0,19):
    url = 'http://maoyan.com/cinemas?offset={}'.format(i*12)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

    }
    ssl_context = ssl._create_unverified_context
    req = request.Request(url,headers=headers)
    response = request.urlopen(req,context=ssl_context)
    content = response.read().decode()
    pattern = re.compile('cinema-info.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?>(.*?)</p>',re.S)
    result = re.findall(pattern,content)
    # print(result)
    with open('maoyan'+str(i)+'.json','a') as f:
        f.write(json.dumps(result,ensure_ascii=False)+'/n')