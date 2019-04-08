import urllib.request as request
import urllib.parse as parse
text = input('请输入你要查找的内容')

startpage = int(input('请输入起始页'))
endpage = int(input('请输入结束页'))

for page in range(startpage,endpage+1):
    data = {
        'wd':text,
        'pn':page*10
    }
    data = parse.urlencode(query=data,encoding='UTF-8')
    url = 'https://www.baidu.com/s?'+data
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
    requests = request.Request(url,headers=headers)
    # data = parse.urlencode(text).encode('UTF-8')
    response = request.urlopen(requests)
    content = response.read()
    with open('meinv'+str(page)+'.html','wb+') as f:
        f.write(content)


# print(response.read().decode())
