import requests
import re
import json
import urllib.parse as parse
def base():
    url = 'https://www.autohome.com.cn/all/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    content = response.content.decode(('gbk'))
    parrern = re.compile('article.*?<li.*?<a.*?href="(.*?)">.*?h3>(.*?)</h3>.*?span.*?>(.*?)</span>.*?/i>(.*?)</em>.*?/i>(.*?)</em>.*?p>(.*?)</p>',re.S)
    result = re.findall(parrern,content)
    for i in result:
        ip = i[0]
        title = i[1]
        timed = i[2]
        eyes = i[3]
        p = i[5]
        dict = {
            'ip':ip,
            'title':title,
            'timed':timed,
            'eyes':eyes,
            'p':p
        }
        with open('car.json','a') as f:
            f.write(json.dumps(dict,ensure_ascii=False)+'\n')
    # print(result)

base()