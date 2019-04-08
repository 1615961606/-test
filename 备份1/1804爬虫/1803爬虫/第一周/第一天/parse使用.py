import urllib.request
import urllib.parse
# word = {
#     'wd':'美女'
# }
# #转换编码
# result = urllib.parse.urlencode(word)
# print(result)
# result = urllib.parse.unquote(result)
# print(result)
url = 'http://www.baidu.com/s'
word = {'wd':'美女'}
word = urllib.parse.urlencode(word)
newurl = url+'?'+word
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'
}
request = urllib.request.Request(newurl,headers=headers)
response = urllib.request.urlopen(request)
content = response.read()
with open('meinv.html','wb+') as f:
    f.write(content)