from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
from lxml import etree
import re
driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

driver.get('https://search.jd.com/Search?keyword=%E8%BE%A3%E6%9D%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E8%BE%A3%E6%9D%A1&stock=1&page=3&s=55&click=0')
# driver.find_element_by_id('key').send_keys('辣条')
driver.find_element_by_class_name('button').click()
time.sleep(10)
driver.find_element_by_xpath('//li[@class="gl-item"]')
html = driver.page_source
content = etree.HTML(html)
# print(type(content))
img_url = content.xpath('//div[@class="p-img"]//@src[1]')
for i in img_url:
    # print(i)
    pass
title = content.xpath('//div[@class="p-name p-name-type-2"]/a/em/text()')
# print(title)
comment = content.xpath('//div[@class="p-commit"]//a/text()')
# print(comment)
dian = content.xpath('//span[@class="J_im_icon"]/a/text()')
# print(dian)
price = content.xpath('//div[@class="p-price"]/strong/i/text()')
print(price)
dict = {
    'img_url':img_url,
    'title':title,
    'comment':comment,
    'dian':dian,
    'price':price

}
# with open('yy.html','w') as f:
#     f.write(html)
# print(type(html))
# parrern = re.compile('p-img.*?img.*?src="(.*?)"')
# result = re.findall(parrern,html)
# for u in result:
#     print(u)