from greenlet import greenlet
import requests
def download_data1():
    print('发起请求1')
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get('https://github.com/',headers=req_headers)
    #会等待响应结果
    download2.switch()
    print('download1下载完',response.status_code)
    download2.switch()
def download_data2():
    print('发起请求2')
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get('https://github.com/',headers=req_headers)
    download1.switch()
    print('download1下载完',response.status_code)


download1 = greenlet(download_data1)
download2 = greenlet(download_data2)
