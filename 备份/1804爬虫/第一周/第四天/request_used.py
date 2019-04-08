#request的使用
import requests

url = 'http://www.baidu.com/'
response = requests.get(url)
response.encoding = 'utf-8'
#h获取状态吗
print(response.status_code)
#获取响应体
html_text = response.text

#如果出现乱码有两种方法
response.encoding = 'utf-8'
#获取响应二进制文件
b_html = response.content.decode()

#获取响应头
response_header = response.headers
#获取相应的编码类型
print(response.encoding)
#获取当前请求的url
response_url = response.url
print(html_text)
print(response_header)
print(response_url)