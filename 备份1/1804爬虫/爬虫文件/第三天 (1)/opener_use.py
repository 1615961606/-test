#自定义opener
from urllib import request

# HTTPSHandler:实例化这个处理器对象，为了支持发起https请求
#debuglevel=1:作用是为了，输出debug日志信息，方便查看请求的请求头等信息
handler = request.HTTPSHandler(debuglevel=1)

# 自定义一个opener
opener = request.build_opener(handler)

#　创建一个Request对象
req = request.Request('https://app.yinxiang.com/')

#　使用opener的open方法发起请求
response = opener.open(req)

print(response.status)
# print(response.read())




# request.urlopen()