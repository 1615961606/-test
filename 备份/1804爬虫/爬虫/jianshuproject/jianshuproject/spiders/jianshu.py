# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from jianshuproject.items import JianshuprojectItem
class JianshuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    #故事 读书 旅行 摄影
    start_urls = ['https://www.jianshu.com/c/fcd7a62be697?order_by=added_at&page=0',
                  'https://www.jianshu.com/c/yD9GAd?order_by=added_at&page=0',
                  'https://www.jianshu.com/c/5AUzod?order_by=added_at&page=0',
                  'https://www.jianshu.com/c/7b2be866f564?order_by=added_at&page=0'
                  ]

    def parse(self,response):
        category = ''
        if response.url.find('fcd7a62be697') >0:
            # print('故事')
            category = '故事'
        elif response.url.find('yD9GAd') >0:
            # print('读书')
            category = '读书'

        elif response.url.find('5AUzod') >0:
            # print('旅行')
            category = '旅行'

        elif response.url.find('7b2be866f564') >0:
            # print('摄影')
            category = '摄影'

        pattern = re.compile('page=(\d+)',re.S)
        page_num = re.findall(pattern,response.url)
        next_page_num = int(','.join(page_num))+1
        pattern1 = re.compile('page=(\d+)')
        next_url = re.sub(pattern1,'page='+str(next_page_num),response.url)
        # print(category)
        yield scrapy.Request(next_url,callback=self.cate_datail,meta={'category':category})

    def cate_datail(self,response):

        category = response.meta['category']
        article_detail = response.xpath('//div[@class="content"]/a/@href').extract()
        for article in article_detail:
            article_detail_url = 'https://www.jianshu.com'+article
            yield scrapy.Request(url=article_detail_url,callback=self.pare_article_page,meta={'category':category})

    def pare_article_page(self,response):
        jian_item = JianshuprojectItem()
        jian_item['tags'] = response.meta['category']

        jian_item['title'] = response.xpath('//h1[@class="title"]/text()').extract()[0]
        jian_item['content'] = response.xpath('//div[@class="show-content-free"]/p/text()').extract()[0]
        jian_item['pub_time'] = response.xpath('//span[@class="publish-time"]/text()').extract()[0]
        jian_item['num_words'] = response.xpath('//span[@class="wordage"]/text()').extract()[0]
        # view_count = response.xpath('//span[@class="views-count"]/text()').extract()
        # comment_count = response.xpath('//span[@class="comments-count"]/text()').extract()
        # likes_count = response.xpath('//span[@class="likes-count"]/text()').extract()
        jian_item['author'] = ','.join(response.xpath('//div[@class="info"]/a/text()').extract()).replace(' ','').replace('\n','').replace(',','')
        jian_item['author_num'] = ','.join(response.xpath('//div[@class="meta"]/span[1]/text()').extract()).replace(' ','').replace('\n','').replace(',','')
        # author_read = ','.join(response.xpath('//div[@class="meta"]/span[2]/text()').extract()).replace(' ','').replace('\n','').replace(',','')
        # author_guan = ','.join(response.xpath('//div[@class="meta"]/span[3]/text()').extract()).replace(' ','').replace('\n','').replace(',','')
        # jian_item['category'] =
        yield jian_item
