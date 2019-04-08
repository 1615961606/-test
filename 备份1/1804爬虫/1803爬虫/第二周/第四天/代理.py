#代理？
# 代理的作用 在做爬虫的过程中，我们访问一个服务器，会找到我们的真是ip，如果请求频率太快，会封掉ip。这个时候我们就需要使用代理服务器，来伪装我们的本机IP。
# 根据协议划分：
# ftp，http，ssl/tsl,socks

# 根据高匿层度划分：
# 高匿代理，普通匿名代理。透明代理，间谍代理。

# 如果我们要使用免费的代理，那么我们要使用高匿代理。
import urllib.request
import random
#使用urllib设置代理

#构建一个简单的ip池
proxy = [
    {'https':'183.64.215.195:59418'},
    {'https':'183.64.215.195:59418'},
    {'https':'183.64.215.195:59418'},
    {'https':'183.64.215.195:59418'},
    {'https':'183.64.215.195:59418'},
    {'https':'183.64.215.195:59418'},
]
proxy_handler = urllib.request.ProxyHandler(
    random.choice(proxy)
)
opener = urllib.request.build_opener(proxy_handler)
form_data = {
    'data1':'value1'
}
form_data = urllib.parse.urlencode(form_data)
# req = urllib.request.Request('https://httpbin.org/post',data=form_data)
req = urllib.request.Request('https://httpbin.org/get')
response = opener.open(req)
print(response.read().decode())

