import requests
import re
import os
from lxml import etree
def wenzhang():
    starttime = int(input('请输入起始页：'))
    endtime = int(input('请输入终止页：'))
    for i in range(starttime,endtime+1):
        url = 'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=%d'%i
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
            }
        response = requests.get(url,headers=headers)

        i = re.compile('<a.*?class="title".*?href="(.*?)">',re.S)
        i = re.findall(i,response.text)                                                      
        for i in i:
            url2 = 'https://www.jianshu.com/' + str(i)
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
                }
            response = requests.get(url2,headers=headers)
            html = etree.HTML(response.text)
            title = re.compile('<h1.*?class="title">(.*?)</h1>',re.S)
            name = re.compile('<div.*?class="info">.*?<a.*?class="title".*?>(.*?)</a>',re.S)
            time = re.compile('<div.*?class="meta".*?<span.*?class="publish-time".*?>(.*?)</span>',re.S)
            content = html.xpath('//div[@class="show-content-free"]/p/text()')
           
            
            title = re.findall(title,response.text)
            name = re.findall(name,response.text)
            time = re.findall(time,response.text)
            
          
            if not os.path.exists('/home/bc/桌面/1803爬虫/第二周/第六天/os/简书/'):
                os.mkdir('/home/bc/桌面/1803爬虫/第二周/第六天/os/简书/')
            else:
                pass
            for t in title:
                abc = title.index(t)
                content1 = ''
                for i in content:
                    content1 = content1+'\n'+i+'\n'
                a_text = '标题:' + t + '\n' + '作者名：' + name[int(abc)] + '\n' + '时间：' + time[int(abc)] + '\n' + '内容：' + content1 + '\n'
              
                b_text = '/home/bc/桌面/1803爬虫/第二周/第六天/os/简书/' + t + '.txt'
                with open(b_text,'w') as f:
                    f.write(a_text)
                    print('成功QAQ!')
              
if __name__ == '__main__':
    wenzhang()