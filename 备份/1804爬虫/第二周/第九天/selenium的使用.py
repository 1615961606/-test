from selenium import webdriver
import time
#创建chrome有界面对象
# driver = webdriver.Chrome(executable_path='/home/bc/桌面/chromedriver')

#创建chrome参数对象
opt = webdriver.ChromeOptions()

#把chrome设置成无界面模式
opt.set_headless()
#创建chrome无界面对象
driver = webdriver.Chrome(options=opt,executable_path='/home/bc/桌面/chromedriver')
#打开浏览器，模拟浏览器请求页面
driver.get('http://www.baidu.com/')
#获取页面信息
html = driver.page_source
#获取id=wrapper标签下的文本内容
data = driver.find_element_by_id("wrapper").text
print(driver.title)
#向百度的搜索框输入关键字
driver.find_element_by_id('kw').send_keys('赵丽颖')
#获取百度搜索按钮，cllick()是模拟点击
driver.find_element_by_id('su').click()
#获取当前页面的cookie()
time.sleep(5)
cookies = driver.get_cookies()
cookie = ''
for item in cookies:
    cookie += item['name']+item['value']+';'
    print(cookie[:-1])
driver.save_screenshot('baidu.png')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
