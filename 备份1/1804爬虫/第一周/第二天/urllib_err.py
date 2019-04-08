from urllib import request,error
req = request.Request('http://www.huohu.com/asdasd.html')
try:
    response = request.urlopen(req)
except error.HTTPError as err:
    print(err.code)
    print(err.reason)
except error.URLError as err:
    print(err.reason)
else:
    print('请求成功')