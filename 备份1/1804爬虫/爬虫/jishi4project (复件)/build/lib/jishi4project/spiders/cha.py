# -*- coding: utf-8 -*-
import scrapy
from jishi4project.items import Jishi4ProjectItem

class ChaSpider(scrapy.Spider):
    name = 'cha'
    allowed_domains = ['chinaz.com']
    start_urls = ['http://top.chinaz.com/']

    def parse(self, response):
        ji_item = Jishi4ProjectItem()
        ji_item['ch_title'] = response.xpath('//dl[@class="MaWebClist"]/dd/a/text()').extract()
        ch_title_url = response.xpath('//dl[@class="MaWebClist"]/dd/a/@href').extract()
        for url in ch_title_url:
            ji_item['ch_title_url'] = url

            z_url = 'http://top.chinaz.com'+url
            yield scrapy.Request(url=z_url,callback=self.parse_detail)

    def parse_detail(self,response):
        ji_item = Jishi4ProjectItem()
        ji_item['image_url'] = response.xpath('//div[@class="leftImg"]/a/@href').extract()
        ji_item['title'] = response.xpath('//h3[@class="rightTxtHead"]/a/text()').extract()[0]
        ji_item['url_name'] = response.xpath('//h3[@class="rightTxtHead"]/span[@class="col-gray"]/text()').extract()[0]
        ji_item['ranking'] = response.xpath('//div[@class="RtCPart clearfix"]/p[1][@class="RtCData"]/a/text()').extract()[0]
        ji_item['lian'] = response.xpath('//div[@class="RtCPart clearfix"]/p[4][@class="RtCData"]/a/text()').extract()[0]
        ji_item['desc'] = response.xpath('//p[@class="RtCInfo"]/text()').extract()[0]
        ji_item['z_ranking'] = ','.join(response.xpath('//strong[@class="col-red02"]/text()').extract())
        ji_item['score'] = ','.join(response.xpath('//div[@class="RtCRateCent"]/span/text()').extract())
        yield ji_item

