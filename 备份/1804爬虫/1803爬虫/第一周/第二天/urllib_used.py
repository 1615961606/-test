import urllib.request
import ssl
import urllib.parse as parse
dict = {
    'q':'美女'
}
dict = parse.urlencode(query=dict,encoding='UTF-8')

url ='https://www.baidu.com/s?'+dict
print(url)
ssl_context  = ssl.create_default_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request,context=ssl_context)
print(response.status)
print(dict)
# print(response.reason)
# print(response.read().decode('UTF-8'))