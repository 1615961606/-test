import urllib.request as request
import urllib.parse as parse
import ssl
url = 'https://fanyi.baidu.com/translate?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
contexts = ssl.create_default_context
fromdata = {
    'from': 'zh',
    'to': 'en',
    'query': '紫色',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '204161.523952',
    'token': '33b76221dcb4c1399e455dcd850f1387',
}
print(fromdata)
fromdata = parse.urlencode(fromdata).encode()
print(fromdata)
req = request.Request(url=url,data=fromdata,headers=headers)
response = request.urlopen(req)
print(response.status)
content = response.read().decode('utf-8')
with open('baidufanyi.html','w+') as f:
    f.write(content)