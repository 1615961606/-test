# -*— coding：UTF-8 -*-
import urllib.request
import randomiphandler
import ssl
import requests

#使用代理发送请求

#首先从数据库中随机获取一个ip
handler = randomiphandler.RandomIpHandler()
ip = handler.get_random_ip()
print(ip)

#构建一个ip地址
proxy = ip['ip']+":"+ip['port']
print(proxy)

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
}

#目标url
url = 'https://www.jianshu.com/p/a5cb4070e733'

#设置代理参数
proxies = {'https': proxy}

#urllib使用代理写法
# proxy_handler = urllib.request.ProxyHandler(proxies) 
# context = ssl._create_unverified_context()
# opener = urllib.request.build_opener(proxy_handler,urllib.request.HTTPSHandler(context=context,debuglevel=1))
# req = urllib.request.Request(url,headers=headers)
# response = opener.open(req)
# if response.code == 200:
#     print('使用'+proxy+"请求成功")

#requests模块使用代理写法
response = requests.get(url, proxies=proxies,headers=headers)
if response.status_code == requests.codes.ok:
    print('使用'+proxy+"请求成功")




