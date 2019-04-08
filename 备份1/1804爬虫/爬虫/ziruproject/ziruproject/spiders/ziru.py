# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ziruproject.items import ZiruprojectItem


class ZiruSpider(CrawlSpider):
    name = 'ziru'
    allowed_domains = ['ziroom.com']
    start_urls = ['http://www.ziroom.com/z/nl/z3.html?p=1']



    def parse_start_url(self, response):
        print(response.status)
    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = resporules = (
        Rule(LinkExtractor(allow=r'.*?p=\d+',restrict_xpaths=('//div[@class="pages"]')), callback='parse_item', follow=True,),
    )nse.xpath('//div[@id="description"]').extract()
        # return i
        ziru_item = ZiruprojectItem()
        names = response.xpath('//div[@class="txt"]/h3/a/text()').extract_first()
        global names
        ziru_item['name'] = names
        ziru_item['adress'] = response.xpath('//div[@class="txt"]/h4/a/text()').extract_first()
        desc1 = response.xpath('//div[@class="detail"]/p[1]/span[1]/text()').extract_first()
        desc2 = response.xpath('//div[@class="detail"]/p[1]/span[2]/text()').extract_first()
        desc3 = response.xpath('//div[@class="detail"]/p[1]/span[3]/text()').extract_first()
        desc4 = response.xpath('//div[@class="detail"]/p[2]/span[1]/text()').extract_first()
        ziru_item['desc'] = desc1+desc2+desc3+desc4
        youdian1 = response.xpath('//p[@class="room_tags clearfix"]/span[1]/text()').extract_first()
        youdian2 = response.xpath('//p[@class="room_tags clearfix"]/span[2]/text()').extract_first()
        youdian3 = response.xpath('//p[@class="room_tags clearfix"]/span[3]/text()').extract_first()
        youdian4 = response.xpath('//p[@class="room_tags clearfix"]/a/span[1]/text()').extract_first()
        ziru_item['youdian'] = youdian1+youdian2+youdian3+youdian4
        # tupian = response.xpath('//div[@class="img pr"]//a/img/@_src').extract()
        # print('===============')
        # for t in tupian:
        #     tt = 'https:'+t
        #
        #     print(tupian)
        #     yield scrapy.Request(url=tt,callback=self.down_images)
        # other_pages = response.xpath('//div[@class="pages"]/a/@href').extract()
        # for t in other_pages:
        #     print('=================')
        #     print(t)
        yield ziru_item
    # def down_images(self,response):
    #     # print(response)
    #     # filename = response.body[-25:-22]
    #     with open('images/'+str(names)+'.jpg','wb+') as f:
    #         f.write(response.body)
            # print('1')

        # print('==========')
        # print(ziru_item)
