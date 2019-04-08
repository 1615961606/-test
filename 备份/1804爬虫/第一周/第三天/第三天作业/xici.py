import urllib.request as request
import random
from urllib import error
import requests
import re
for i in range(1,50):
    url = 'http://www.xicidaili.com/nn/{}'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }
    response = requests.get(url,headers=headers)
    content = response.content.decode()
    # print(content)
    parrern = re.compile('country.*?<img.*?>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<a.*?>(.*?</a>)',re.S)
    all_xi_url = re.findall(parrern,content)
    proxy_lists = []
    for p in all_xi_url:
    # print(all_xi_url) 
        proxy_lists.append(p[0])
        # print(proxy_lists)
    for uuu in proxy_lists:
        # print(uuu)
        proxy_list = [
            {"http"  : uuu},
        ]
    for i in proxy_list:
        prxoy = random.choice(proxy_list)
        httpproxy_handler = request.ProxyHandler(prxoy)

        opener = request.build_opener(httpproxy_handler)
        req = request.Request('http://httpbin.org/get')

        try:
            response = opener.open(req,timeout=2)
        except error.HTTPError as err:
            print(err.code)
            print(err.reason)
        except error.URLError as err:
            print(err.reason)
        else:
            print('请求成功')