import urllib.request as request

#Request的使用
#如果要使用请求头，直接使用urlopen不能够实现
# 这个时候需要先创建一个Ruquest对象然后发起请求


# request.Request()
# data=默认为none,表示get请求，一旦不能为none,表示post请求
# headers：设置请求头，是一个字典类型的参数
# origin_req_host：远端主机的host
# method：设置请求的方式

#构建一个请求头
url = 'http://www.httpbin.org/get'
req_headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
#构造一个请求对象
req = request.Request(url,headers=req_headers)

response = request.urlopen(req)
content = response.read().decode()
print(content)
print(response.status)