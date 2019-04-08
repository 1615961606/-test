
from selenium import webdriver
from lxml import etree
import requests
opt = webdriver.ChromeOptions()
opt.set_headless()

def daxues():
    driver = webdriver.Chrome(options=opt, executable_path='/home/bc/桌面/chromedriver')
    driver.get('http://faculty.hust.edu.cn/pyjs.jsp?urltype=tsites.PinYinTeacherList&wbtreeid=1001&py=f&lang=zh_CN')
    html = driver.page_source
    htmls = etree.HTML(html)
    name = htmls.xpath('//ul[@class="pic-list clearfix"]/li/a/@href')
    print('============')
    for i in name:
            
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
        response = requests.get(i,headers=headers)
        print(response)

if __name__ == '__main__':
    daxues()
    
  