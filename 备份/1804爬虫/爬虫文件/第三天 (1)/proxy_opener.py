#由于urlopen不支持代理，而爬虫往往需要设置代理方对方的服务器
#所有我们需要自定义opener，让我们发起请求的时候可以携带代理

from urllib import request

#第一步创建handler处理器
proxy_handler = request.ProxyHandler(
    {
        'http':'118.190.95.35:9001',
        'https':'182.88.4.142:8123',
    }
)

#自定义opener
opener = request.build_opener(proxy_handler)

# req = request.Request('http://www.baidu.com/')
req = request.Request('https://httpbin.org/get')

#使用opener.open()方法发送请求，就会携带我们设置的代理了
response = opener.open(req)

print(response.status)
print(response.read().decode('utf-8'))

