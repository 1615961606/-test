# -*- coding: utf-8 -*-
import scrapy

class BaiduSpider(scrapy.Spider):
    #爬虫的名称
    name = 'baidu'
    #在这里设置爬虫允许爬取的域,可以是多个.
    allowed_domains = ['baidu.com']
    #我们在这里设置爬虫的起始url
    start_urls = ['http://baidu.com/']

    #解析方法（回调方法）
    def parse(self, response):
        """"
        response:请求成功后,得到的响应结果
        """
        #获取响应的状态码
        status_code = response.status
        print('响应结果：',status_code)
        #还可以获取响应的文本
        html_text = response.text
        # print(html_text)
        #获取二进制数据
        b_text = response.body
        # print(b_text)
        #获取当前请求的url
        current_url = response.url

        print(current_url)



        pass

