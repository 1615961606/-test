import requests,gevent
from gevent import monkey,pool
def download(url):
    print(url+'正在下载1')
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    response = requests.get(url,headers=header)
    print(len(response.text),url+'已完成１')

monkey.patch_all()

def download2(url):
    print(url+'正在下载2')
    header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
    response = requests.get(url,headers=header)
    print(len(response.text),url+'已完成2')

pool = pool.Pool(3)
gevent.joinall(
    [
        pool.spawn(download,'https://www.yahoo.com/'),
        pool.spawn(download,'https://www.taobao.com/'),
        pool.spawn(download,'https://github.com/'),
        pool.spawn(download2,'https://www.yahoo.com/'),
        pool.spawn(download2,'https://www.taobao.com/'),
        pool.spawn(download2,'https://github.com/'),
    ]
)