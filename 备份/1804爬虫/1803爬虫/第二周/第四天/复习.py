import urllib.request as request
import urllib.parse as parse
#第一种
# data=发起post请求的时候使用这个参数
# timeout=设置超时的时间
# context 忽略ssl证书
kw = {
    'kw':'中文网'
}
kw = parse.urlencode(kw)
response = request.urlopen('https://www.baidu.com',timeout=5)


#最基本的get请求

#获取那些数据
print(response.status)
print(response.getheaders())
print(response.reason)

post请求
表单数据
fromdata = {
    'data1':'value1',
    'data2':'value2',
    'data3':'value3',

}
fromdata = parse.urlencode(fromdata).encode()
request.urlopen('https://www.baidu.com')
headers = {
    'User-Agent':'',
    'cookies':'',
    'Referer':'',
}
req = request.Request('https://www.baidu.com'data=fromdata,headers=headers,method=POST)
response = request.urlopen(req)

#状态吗：
200：表示成功
3xx：重定向
4xx：客户端错误
    400：请求错误
    401：需要用户认证
    403：用户权限
    404：找不到网页
    405：请求方式不正确
    407：代理相关错误
    408：请求超时
500：服务端错误