# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['baidu.com']
    # 设置起始url,内部如何发起请求的？？？？
    start_urls = ['https://github.com/yuemeiss']

    #自定义settings.py中的参数设置,
    #优先级比settings.py文件中设置的参数要高
    custom_settings = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    #自定义起始url回调方法：
    def start_requests(self):
        # 使用场景：当你访问某个网站的时候，必须要登录之后，才可以获取数据
        # 这时我们需要要重写start_requests,在这个方法里面模拟登录，获取
        # coolies.

        #模拟登录
        driver = webdriver.Chrome(executable_path='/home/ljh/桌面/driver/chromedriver')
        #打开github登录页面
        driver.get('https://github.com/login')
        driver.implicitly_wait(10)
        #添加账号，密码
        driver.find_element_by_id('login_field').send_keys('yuemeiss')
        driver.find_element_by_id('password').send_keys('xian49901.d')
        #点击登录按钮
        driver.find_element_by_name('commit').click()

        #获取cookies
        cookies = driver.get_cookies()

        cookies_dict = {note['name']:note['value'] for note in cookies}

        print(cookies_dict)

        for url in self.start_urls:

            yield scrapy.Request(url=url,cookies=cookies_dict,dont_filter=True,callback=self.custome_parse)


    def custome_parse(self,response):

        with open('page.html','w') as file:
            file.write(response.text)

        print(response.status)

    # def parse(self, response):
    #     pass
