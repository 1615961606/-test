import urllib.request as request
import urllib.parse as parse

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
form_data = {
    'i': '美女',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom':'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false'
}
form_data = parse.urlencode(form_data).encode()
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
req = request.Request(url,headers=req_headers)
response = request.urlopen(req)
print(response.read().decode())