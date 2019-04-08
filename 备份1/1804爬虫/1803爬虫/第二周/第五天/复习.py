#代理?
# 目的：防止被封ip
# 协议分类 高匿 普通匿名

# 如何去使用代理？
# 自定义opener
import urllib.request

# 自定义代理的处理器（）
proxy_handle = urllib.request.ProxyHandler(
    {'https':':port',
    'http':'ip:port'}
)

#自定义opener
urllib.request.urlopen
opener = urllib.request.build_opener(proxy_handle)

# 构造一个request对象
req  = urllib.request.Request('https://httpbin.org/get')
# 发起请求
response = opener.open(req,timeout=5)
print(response.status)