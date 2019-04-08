import requests
# url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
#     'Referer': 'https://www.lagou.com/jobs/list_java?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='

# }
# form_data = {
#     'first':'false',
#     'pn':1,
#     'kd':'ios'

# }
# response = requests.post(url,data=form_data,headers=headers)
# print(response.status_code)
# print(response.text)
# print(type(response.json()))
# if response.status_code == requests.codes.ok:
#     print('请求成功')

#上传文件
# url = 'https://httpbin.org/post'
# file = {'file':open('cookies.text','r')}
# response = requests.post(url,files=file)
# print(response.status_code)
# print(response.json())

#网页需要验证
response = requests.post('https://www.nxjsjcndcd.com/',data=formdata,)

