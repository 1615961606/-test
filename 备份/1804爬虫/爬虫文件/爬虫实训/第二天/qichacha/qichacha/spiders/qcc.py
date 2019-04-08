# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from qichacha.items import QichachaClassfyItem

class QccSpider(scrapy.Spider):
    name = 'qcc'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.qichacha.com/']
    """
    step:根据https://www.qichacha.com/找到分类的信息,存入数据库
    """

    def parse(self, response):

        print(response.status)

        classifies = response.xpath('//li[@class="area  text-center"]')

        for li in classifies:
            #分类的item
            classify_item = QichachaClassfyItem()
            #标题
            classify_item['classifyName'] = li.xpath('./a/text()').extract_first('')
            #分类id
            classify_item['sign'] = li.xpath('./a/@href').extract_first('').replace('/','')
            #获取每一分类下第一页的url地址
            #样例：https://www.qichacha.com/g_AH.html
            #first_page_url = response.urljoin(classify_item['sign']+".html")
            first_page_url = 'https://www.qichacha.com/'+ classify_item['sign'] + ".html"
            classify_item['firstUrl'] = first_page_url

            yield classify_item

            yield scrapy.Request(
                url=first_page_url,
                meta={
                    'classifyName':classify_item['classifyName'],
                    'sign':classify_item['sign'],
                },
                callback=self.parse_company_list
            )

    def parse_company_list(self,response):
        pass