#urllib如何使用cookies
from http import cookiejar 
from urllib import request

#方式１
#1.直接在请求头中设置cookies

#方式２
# 1.可以创建cookiejar对象来管理，存储cookie值
req_cookiejar = cookiejar.CookieJar()

#2.创建HTTPCookieProcessor处理器，来管理cookiejar对象
cookie_handler = request.HTTPCookieProcessor(req_cookiejar)

#3.自定义opener对象
opener = request.build_opener(cookie_handler)

#根据自定义的opener发起请求
req = request.Request('http://www.baidu.com/')

opener.open(req)

req1 = request.Request('http://www.baidu.com/')

opener.open(req1)

print(type(req_cookiejar))

print(req_cookiejar)

for cookie in req_cookiejar:
    print(cookie.name,cookie.value)





