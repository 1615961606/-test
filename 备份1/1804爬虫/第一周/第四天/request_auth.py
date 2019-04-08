#有些网站在第一次访问的时候需要输入账号，密码

import requests
response = requests.get('网址',auth=('账号','密码'))

print(response.status_code)
print(response.text)