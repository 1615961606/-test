import urllib.request
import urllib.parse as parse
url = 'http://fanyi.youdao.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}
data = parse.urlencode(formdata).encode('utf-8')
request = urllib.request.Request(url, data = data, headers = headers)
response = urllib.request.urlopen(request)
content = response.read()
with open('youdao.html','wb+') as f:
    f.write(content)
