import requests
# http://www.renren.com/PLogin.do
#利用session进行会话维持

#创建一个session对象(之后发起请求获取到的cookie值会保存在session)
session = requests.session()

#发起请求
url = 'http://www.renren.com/PLogin.do'
form_data = {
    'email':'18334521201',
    'password':'mya1314.'
}
req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = session.post(url,data=form_data,headers=req_headers)
print(response.status_code)
#登录成功后，获取个人主页数据
url = 'http://www.renren.com/968382677/profile'
session.get(url,headers=req_headers)
print(response.status_code)
print(response.text)