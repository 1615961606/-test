import urllib.request as request
import random
from urllib import error
# httpproxy_handler = request.ProxyHandler(
#     {
#         'http':'222.221.11.119:3128',
#         'https':'125.32.233.215:8118'
#     }
# )
proxy_list = [
    {"http"  : "121.31.177.164"},
    {"http"  : "118.190.95.35"},

]
for i in proxy_list:
    prxoy = random.choice(proxy_list)
    httpproxy_handler = request.ProxyHandler(prxoy)

    opener = request.build_opener(httpproxy_handler)
    req = request.Request('http://httpbin.org/get')
    # request.install_opener(opener)
    # response = request.urlopen(req)
    try:
        response = opener.open(req,timeout=3)
    except error.HTTPError as err:
        print(err.code)
        print(err.reason)
    except error.URLError as err:
        print(err.reason)
    else:
        print('请求成功')
    # print(response.read().decode())