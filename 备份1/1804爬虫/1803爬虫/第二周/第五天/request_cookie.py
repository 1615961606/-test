#request关于cookie的使用
import requests
#百度
response = requests.get('https://www.baidu.com')
print(response.status_code)
print(response.cookies.items())
cookies = {}
for cookie in response.cookies.items():
    print(type(cookie))
    print(cookie)

    print(cookie[0]+'='+cookie[1])
    cookies[cookie[0]=cookie[1]]

#使用cookie的方式
# 方式一：可以将cookie放在请求头中
# 方式二：可以使用请求的参数
resppnse = requests.get('https://www.baidu.com',cookies=cookies)
print(response.status_code)

##Cookiejar object
cookiesjar = requests.cookies.RequestsCookieJar()

for name,value in cookies.items()
    cookiesjar.set(name,value)
response = requests.get('https://www.baidu.com',cookies=cookiesjar)