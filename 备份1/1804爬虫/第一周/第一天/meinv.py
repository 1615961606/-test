import urllib.request as request
import urllib.parse as parse
import ssl
con = input('请输入你要搜索的关键字')
startpage = int(input('请输入起始页面'))
endpage = int(input('请输入终止页面'))
for i in range(startpage-1,endpage):
    data = {
        'wd':con,
        'pn':i*10
    }
    data = parse.urlencode(query=data,encoding='utf-8')
    url = 'https://www.baidu.com/s?'+data
    result = parse.urlparse(url)
    print(result)
    context = ssl._create_unverified_context()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }
    req = request.Request(url,headers=headers)
    response = request.urlopen(req,context=context)
    content = response.read().decode()
        #获取响应头信息
        # response_headers = response.getheaders()
        #获取某一个字段的信息
        # response_server = response.getheader('Server')
    with open('baidu.html','w') as f:
        f.write(content)
    # print(content)