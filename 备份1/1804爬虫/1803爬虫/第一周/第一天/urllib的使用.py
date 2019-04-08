import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
text = response.read()
print(text)
print(response.status)
print(response.getheaders())