import requests
#设置代理
proxy = {
    'http':'218.65.254.114',
    'https':'175.148.72.52:1133'
}
url = 'https://httpbin.org/get'
response = requests.get(url,proxies=proxy)
print(response.status_code)
print(response.text)
#使用私密代理
# proxy = {
#     'http':''
# }