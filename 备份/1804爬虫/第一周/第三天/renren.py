from urllib import request
import http.cookiejar as cookiejar
from urllib import parse

#创建一个cookie对象
req_cookiejar = cookiejar.CookieJar()

#创建一个cookiejar的管理器对象HTTPprocessor
handle = request.HTTPCookieProcessor(req_cookiejar)

#自定义opneer
opener = request.build_opener(handle)
# http://www.renren.com/PLogin.do

form_data = {
    'email':'18334521201',
    'password':'mya1314.'
}

form_data = parse.urlencode(form_data).encode('utf-8')
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}
req = request.Request('http://www.renren.com/PLogin.do',headers=req_headers,data=form_data)

response = opener.open(req)
print(response.status)
for cookie in req_cookiejar:
    print(cookie.name+'='+cookie.value)

req2 = request.Request('http://www.renren.com/968382677/profile',headers=req_headers)
response = opener.open(req2)
print(response.code)
html = response.read()

with open('renren.html','wb') as f:
    f.write(html)