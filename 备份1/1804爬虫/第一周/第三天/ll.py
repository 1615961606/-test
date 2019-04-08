import urllib.request
import random

proxy_list = [
{"https" : "124.88.67.81:80"},
{"https" : "124.88.67.81:80"},
{"https" : "124.88.67.81:80"},
{"https" : "124.88.67.81:80"},
{"http" : "59.44.78.30"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 使用选择的代理构建代理处理器对象
httpproxy_handler = urllib.request.ProxyHandler(proxy)

opener = urllib.request.build_opener(httpproxy_handler)

request = urllib.request.Request("http://httpbin.org/get")
response = opener.open(request)
print (response.read())