import requests

#获取cookie
response = requests.get('http://www.baidu.com')

#可以直接从响应中获取cookiejar、
cookiejar = response.cookies
print(type(cookiejar))

#将cookjar转换成字典类型的数据
cookie_dict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookie_dict)

#发送请求的时候设置cookie
#cookies这个参数可以设置一个字典，也可以设置一个cookjar对象
response= requests.get('http://www.baidu.com',cookies=cookiejar)
print(response.status_code)