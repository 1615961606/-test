import urllib
import ssl
# urllib.request.urlopen

#构建一个HTTPHandler(),支持请求http协议的接口
context = ssl._create_unverified_context()
http_handler = urllib.request.HTTPHandler()
https_handler = urllib.request.HTTPSHandler(context=context)


opener = urllib.request.build_opener(http_handler,https_handler)
response = opener.open('https://www.baidu.com')
print(response.status)