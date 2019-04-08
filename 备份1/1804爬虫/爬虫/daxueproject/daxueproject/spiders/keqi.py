# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from lxml import etree
class KeqiSpider(scrapy.Spider):
    name = 'keqi'
    allowed_domains = ['faculty.hust.edu.cn']
    start_urls = ['http://faculty.hust.edu.cn/pyjs.jsp?urltype=tsites.PinYinTeacherList&wbtreeid=1001&py=f&lang=zh_CN']

    def parse(self, response):
        opt = webdriver.ChromeOptions()
        opt.set_headless()

        driver = webdriver.Chrome(options=opt, executable_path='/home/bc/桌面/chromedriver')
        driver.get('http://faculty.hust.edu.cn/pyjs.jsp?urltype=tsites.PinYinTeacherList&wbtreeid=1001&py=f&lang=zh_CN')
        html = driver.page_source
        htmls = etree.HTML(html)
        name = htmls.xpath('//ul[@class="pic-list clearfix"]/li/a/@href')
        print('============')


        print(name)
        # print(html)
        # d_url = response.xpath('//ul[@class="pic-list clearfix"]/li/a/@href').extract_first()
        # l_url = response