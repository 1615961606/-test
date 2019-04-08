# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    adreess = scrapy.Field()
    job_name = scrapy.Field()
    company_name = scrapy.Field()
    wage = scrapy.Field()
    pub_time = scrapy.Field()
    require = scrapy.Field()
    welffare = scrapy.Field()
    desc = scrapy.Field()
    enterprise_desc = scrapy.Field()

