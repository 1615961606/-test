# xpath语法：
# #
# from lxml import etree

# #构建一个xpath的解析器对象
# xp_html = etree.HTML()

# #直接获取某一个标签（li）
# li_list = xp_html.xpath('//li')

# #要根据class来获取对应的标签
# xp_html.xpath('//div[@class="值"]')

# #要根据id来获取对应的标签
# xp_html.xpath('//div[@id="值"]')

# 什么时候使用'/' ? :从根目录查找
# <div>
#   <ul>
#        <li>
#           <a>
#           </a>
#        </li>
#   </ul>
# </div>
# 要获取div下的ul标签
# xp_html.xpath('//div/ul')


# 什么时候使用'//' ? :无论你要获取的标签在什么位置，使用//都可以匹配出来
# 要想直接从div下获取li标签
# xp_html.xpath('//div//li')
# xp_html.xpath('//div//a')

# #@符号，后面添加属性名称，表示获取某一个标签的属性值
# xp_html.xpath('//a/@href')

# #text():表示获取某一个标签的文本
# xp_html.xpath('//a/text()')

# # . 表示从当前节点获取标签

# #在多个标签中，想要获取某一个指定位置的标签
# xp_html.xpath('//ul/li[2]')
# xp_html.xpath('//ul/li[last()]')
# xp_html.xpath('//ul/li[last()-1]')


#除了xpath之外,我们介绍beatifulsoup
from bs4 import BeautifulSoup
import requests

#以腾讯招聘为例子



def tencentjobspider():
    #https://hr.tencent.com/position.php?&start=0
    #https://hr.tencent.com/position.php?&start=10
    url = 'https://hr.tencent.com/position.php?&start=0'
    req_headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    }
    response = requests.get(url,headers=req_headers)

    #１．要使用它,首先需要构建一个beautifulsoup对象
    soup = BeautifulSoup(response.text,'lxml')

    #获取职位列表
    #name:标签的名称
    #attrs={}：要获取标签的属性
    job_even = soup.find_all(name='tr',attrs={'class':'even'})
    print(len(job_even))
    job_odd = soup.find_all(name='tr',attrs={'class':'odd'})
    print(len(job_odd))

    # job_even = soup.find_all(class_='even')
    # job_even = soup.find_all(id='even')

    for job_note in job_even+job_odd:
        #css选择器
        # (.　表示类：class
        # (#  表示id)
        # jobtitle = job_note.select('td.l.square a')[0].string
        jobtitle = job_note.select('td.l.square a')[0].get_text()
        jobtype = job_note.select('td')[1].string
        needpeople = job_note.select('td')[2].string
        jobadress = job_note.select('td')[3].string
        publishtime = job_note.select('td')[4].string
        #获取标签的属性值
        job_url = job_note.select('td.l.square a')[0].attrs['href']
        print(job_url)


        # print(type(jobtitle))
        # print(jobtitle)

    
if __name__ == '__main__':
    tencentjobspider()
    



