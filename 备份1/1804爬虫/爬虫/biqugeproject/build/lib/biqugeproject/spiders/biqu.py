# -*- coding: utf-8 -*-
import scrapy


from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from biqugeproject.items import BiqugeprojectItem

class BiquSpider(CrawlSpider):
    name = 'biqu'
    allowed_domains = ['hehuamei.com']
    start_urls = ['https://www.hehuamei.com/xuanhuanxiaoshuo/',
                  'https://www.hehuamei.com/xiuzhenxiaoshuo/',
                  'https://www.hehuamei.com/dushixiaoshuo/',
                  'https://www.hehuamei.com/chuanyuexiaoshuo/',
                  'https://www.hehuamei.com/wangyouxiaoshuo/',
                  'https://www.hehuamei.com/kehuanxiaoshuo/']


    rules = (
        Rule(LinkExtractor(allow=r'.*?com\/.*?\/(.*?)',restrict_xpaths='//div[@class="pagelink"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def parse_start_url(self, response):
        title_url = response.xpath('//span/a/@href').extract()
        category = ''
        for i in title_url:
            next_url = 'https://www.hehuamei.com'+i
            # print(response.url)
            if response.url.find('xuanhuanxiaoshuo') > 0:
                category = '玄幻小说'
            elif response.url.find('xiuzhenxiaoshuo') > 0:
                category = '修真小说'
            elif response.url.find('dushixiaoshuo') > 0:
                category = '都市小说'
            elif response.url.find('chuanyuexiaoshuo') > 0:
                category = '穿越小说'
            elif response.url.find('wangyouxiaoshuo') > 0:
                category = '网游小说'
            elif response.url.find('kehuanxiaoshuo') > 0:
                category = '科幻小说'
            yield scrapy.Request(url=next_url,callback=self.parse_artitle_list,meta={'category':category})

    def parse_artitle_list(self,response):
        category = response.meta['category']
        all_article_detail_url = response.xpath('//div[@id="list"]/dl/dd/a/@href').extract()
        for url in all_article_detail_url:
            article_content_url = 'https://www.hehuamei.com'+url
            yield scrapy.Request(url=article_content_url,callback=self.get_article_content,meta={'category':category})

    def get_article_content(self,response):
        biqugeitem = BiqugeprojectItem()

        # print(response.text)
        biqugeitem['title'] = response.xpath('//div[@class="con_top"]/a[2]/text()').extract_first()
        biqugeitem['article_name'] = response.xpath('//div[@class="bookname"]/h1/text()').extract_first()
        biqugeitem['article_content'] = ','.join(response.xpath('//div[@id="content"]/text()').extract()).replace(' ','').replace('\n','').replace('\xa0\xa0\xa0\xa0','')
        biqugeitem['tags'] = response.meta['category']
        # print(biqugeitem['tags'])
        yield biqugeitem
