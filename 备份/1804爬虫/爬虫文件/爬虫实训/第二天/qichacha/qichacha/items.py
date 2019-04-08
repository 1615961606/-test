# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QichachaClassfyItem(scrapy.Item):
    #分类的字段
    #分类名称
    classifyName = scrapy.Field()
    #分类的表示
    sign = scrapy.Field()
    #首页列表地址
    firstUrl = scrapy.Field()




