# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Jishi4ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # image_url = scrapy.Field()
    title = scrapy.Field()
    # url_name = scrapy.Field()
    # ranking = scrapy.Field()
    # lian = scrapy.Field()
    # desc = scrapy.Field()
    # z_ranking = scrapy.Field()
    # score = scrapy.Field()


class first_page_Item(scrapy.Item):
    ch_title = scrapy.Field()
    ch_title_url = scrapy.Field()
