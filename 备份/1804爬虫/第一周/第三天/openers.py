#自定义opener
import urllib.request as request
#构建一个处理对象，支持处理http请求
http_handler = request.HTTPHandler(debuglevel=1)
https_handler = request.HTTPSHandler(debuglevel=1)
#调用build_opener()方法
openr = request.build_opener(https_handler)

req = request.Request('https://www.baidu.com/')
response = openr.open(req)
# response = request.urlopen(req)
print(response.read().decode())
