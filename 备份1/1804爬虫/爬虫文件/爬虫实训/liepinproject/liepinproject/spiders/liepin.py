# -*- coding: utf-8 -*-
import scrapy
from liepinproject.items import LiepinprojectItem

class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?init=-1&headckid=dc6b7959bbc2ef0f&fromSearchBtn=2&ckid=dc6b7959bbc2ef0f&degradeFlag=0&key=python&siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_industry&d_ckId=4218f463eac6e7545b0c00b859a4d6c6&d_curPage=0&d_pageSize=40&d_headId=4218f463eac6e7545b0c00b859a4d6c6&curPage=1']

    def parse(self, response):
        # print(response.status)

        title = ','.join(response.xpath('//div[@class="job-info"]/h3/a/text()').extract()).replace('\t','')
        a_url = response.xpath('//div[@class="job-info"]/h3/a/@href').extract()
        for url in a_url:
            if 'https' not in url:
                continue
            yield scrapy.Request(url=url,callback=self.detail_page)

        next_page = response.xpath('//div[@class="pagerbar"]/a/@href').extract()
        for page_url in next_page:
            page_url = 'https://www.liepin.com'+page_url
            yield scrapy.Request(url=page_url,callback=self.parse)

    def detail_page(self,response):
        liepin_item = LiepinprojectItem()
        liepin_item['adreess'] = response.xpath('//p[@class="basic-infor"]/span/a/text()').extract_first()
        liepin_item['job_name'] = response.xpath('//div[@class="title-info"]/h1/text()').extract_first()
        liepin_item['company_name'] = response.xpath('//div[@class="title-info"]/h3/a/text()').extract_first()
        liepin_item['wage'] = response.xpath('//p[@class="job-item-title"]/text()').extract_first().replace(' ','')
        liepin_item['pub_time'] = response.xpath('//time/text()').extract_first().replace('\r','').replace('\n','')
        liepin_item['require'] = ','.join(response.xpath('//div[@class="job-qualifications"]//span//text()').extract())
        liepin_item['welffare'] = '.'.join(response.xpath('//ul[@class="comp-tag-list clearfix"]//li//span/text()').extract())
        liepin_item['desc'] = ','.join(response.xpath('//div[@class="content content-word"]//text()').extract()).replace(' ','').replace('\n','').replace('\r','').replace('\t','')
        liepin_item['enterprise_desc'] = ','.join(response.xpath('//div[@class="info-word"]/text()').extract()).replace('\n','').replace('\r','').replace(' ','')
        yield liepin_item