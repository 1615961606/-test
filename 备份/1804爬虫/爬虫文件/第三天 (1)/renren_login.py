from urllib import request,parse
from http import cookiejar

#1.创建一个cookiejar对象
req_cookiejar = cookiejar.CookieJar()

#2.创建一个cookiejar的管理器对象，HTTPCOokieProcessor
handler = request.HTTPCookieProcessor(req_cookiejar)

#3.自定义opener 
opener = request.build_opener(handler)

#使用opener的open方法发起请求
# 目标url:http://www.renren.com/PLogin.do
#        http://www.renren.com/PLogin.do
form_data = {
    'email':'18516820311',
    'password':'123456',
}

form_data = parse.urlencode(form_data).encode('utf-8')

#发起请求
req_header = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
req = request.Request(
    'http://www.renren.com/PLogin.do',
    data=form_data,headers=req_header)

response = opener.open(req)

print(response.status)

for cookie in req_cookiejar:
    print(cookie.name+'='+cookie.value)

#访问个人主页：http://www.renren.com/968382671/profile
req2 = request.Request('http://www.renren.com/968382671/profile',headers=req_header)

response = opener.open(req2)

print(response.status)

#将获取到的个人主页源码保存在本地，和浏览器做比对
with open('profile.html','w') as file:
    file.write(response.read().decode('utf-8'))



