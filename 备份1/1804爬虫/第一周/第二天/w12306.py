#获取贴吧的美女吧，里面的详情页面
import urllib.request as request
import urllib.parse as parse
def tiebas(keyword,startpage,endpage):
    for i in range(startpage,endpage+1):
        data = {
            'kw':keyword,
            'ie':'utf-8',
            'pn':(i-1)*50
        }
        data = parse.urlencode(data)
        print(data)
        url = 'https://tieba.baidu.com/f?'+data
        page_name = '第'+str(i)+'页.html'
        downpage(url,page_name)
        

def downpage(url,page_name):
    req_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }
    req = request.Request(url,headers=req_headers)
    response = request.urlopen(req)
    status = response.status
    if status == 200:
        htmldata = response.read().decode()
   
if __name__ == '__main__':
    keyword = input('请输入你要搜索的贴吧名称')
    startpage = int(input('请输入起始页码'))
    endpage = int(input('请输入终止页码'))
    tiebas(keyword,startpage,endpage)