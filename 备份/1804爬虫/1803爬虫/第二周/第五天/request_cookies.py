#cookies
#http/https请求是无状态的请求，为了状态保持，有了cookies和session
#cookies：保存在客户端的
#session保存在服务端
#cookies的属性：name，value，domain，path，amx-age。size
#请求头中的cookie：name=value；name=value；..

#百度为例子
import urllib.request
from http import cookiejar

#创建一个cookiejsar,来储存cookie,保存在内存中
# http_cookie = cookiejar.CookieJar()
# 创建一个handle来处理cookie
# processor = urllib.request.HTTPCookieProcessor(http_cookie)
# 自定义opener
# opener = urllib.request.build_opener(processor)

# 使用opener发起请求
# response = opener.open('https://www.baidu.com')
# print(response.status)
# print(http_cookie)
# print(type(http_cookie))

# for cookie in http_cookie:
#     print(cookie.name+'='+cookie.value)
# response = opener.open('https://www.baidu.com/s?wd=%E8%A5%BF%E5%88%BA%E4%BB%A3%E7%90%86')
#使用
filename = 'cookies.text'
#创建一个mozilla对象来存储cookie
mz_cookie = cookiejar.MozillaCookieJar(filename)

processor =  urllib.request.HTTPCookieProcessor(mz_cookie)

# 自定义opener
opener = urllib.request.build_opener(processor)

# 使用opener发起请求
response = opener.open('https://www.baidu.com')

mz_cookie.save()

如何使用本地的cookie文件
filename = 'cookies.text'
mz_cookie = cookiejar.MozillaCookieJar(filename)
mz_cookie.load(filename)
print(mz_cookie)
processor =  urllib.request.HTTPCookieProcessor(mz_cookie)

# 自定义opener
opener = urllib.request.build_opener(processor)

# 使用自定义的opener发起请求
response = opener.open('https://www.baidu.com')

urllib.request.install_opener(opener)

