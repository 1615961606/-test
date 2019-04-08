import urllib.request as request
import urllib.parse as parse

url = 'http://httpbin.org/post'

form_data = {
    'name':'旱地',
    'age':'22',
    'gender':'女',
}
#encode将字符串类型转换成二进制
form_data = parse.urlencode(form_data).encode()
print(form_data)

req = request.Request(url,data=form_data)

#发起请求
response = request.urlopen(req)
print(response.read().decode())
print(response.status)