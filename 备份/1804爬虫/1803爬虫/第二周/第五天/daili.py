import requests
import requests.exceptions as exceptions
proxies = {
    'https':'115.46.99.27:8123',
    'http':'118.190.199.55:80',

    
}#代理，如何设置代理
try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.status_code)
    print(response.text)
except exceptions.ConnectTimeout as err:
    print(err)
