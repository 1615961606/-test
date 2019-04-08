import requests
parms= {
    'wd':'西刺',
}
response = requests.get('https://www.baidu.com',parms)
print(response.status_code)
# print(response.text)
print(response.content.decode())