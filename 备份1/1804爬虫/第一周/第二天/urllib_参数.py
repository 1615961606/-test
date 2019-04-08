import urllib.request as request
import urllib.parse as parse

data = {
    'wd':'美女',
    'name':'赵丽颖'
}
data = parse.urlencode(data)
url = 'https://www.baidu.com/s?'+data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}
req = request.Request(url,headers=headers)
response = request.urlopen(req)
print(response.status)
# print(data)