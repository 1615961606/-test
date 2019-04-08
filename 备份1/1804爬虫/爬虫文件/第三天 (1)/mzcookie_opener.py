#有时候我们需要将获取到的cookie保存在本地文件中，
# 我们需要使用到MozillaCookieJar

from http import cookiejar
from urllib import request

#１设置一个文件名，将cookie保存在这个文件下
filename = 'cookie.txt'
#２．创建一个cookiejar对象，用来管理和存储cookie
mz_cookiejar = cookiejar.MozillaCookieJar(filename)
#3.创建一个HTTPCookieprocessor处理器对象，管理cookiejar
handler = request.HTTPCookieProcessor(mz_cookiejar)

#自定义一个opener
opener = request.build_opener(handler)

#使用opener对象发起请求
req = request.Request('http://www.baidu.com/')

response = opener.open(req)

print(response.status)

#使用save方法，保存cookie
mz_cookiejar.save()