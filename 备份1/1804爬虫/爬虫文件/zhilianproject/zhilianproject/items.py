# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobname = scrapy.Field()
    salary = scrapy.Field()
    companyName = scrapy.Field()
    adress = scrapy.Field()
    workyear = scrapy.Field()
    degree = scrapy.Field()
    needpeople = scrapy.Field()
    jobinfo = scrapy.Field()
    companyUrl = scrapy.Field()
    jobUrl = scrapy.Field()

class ZhiliancompanyItem(scrapy.Item):
    pass
