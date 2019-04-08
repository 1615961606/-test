from http import cookiejar
from urllib import request
file_name = 'cookie.text'
ma_cookie = cookiejar.MozillaCookieJar(file_name)
#创建一个处理对象，管理cookjar
handle = request.HTTPCookieProcessor(ma_cookie)

opener = request.build_opener(handle)

req = request.Request('http://www.baidu.com/')

response = opener.open(req)
print(response.status)
ma_cookie.save()