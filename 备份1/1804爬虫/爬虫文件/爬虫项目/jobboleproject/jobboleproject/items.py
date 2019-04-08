# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #创建时间
    create_date = scrapy.Field()
    #王章地址
    url = scrapy.Field()
    #id
    url_object_id = scrapy.Field()
    #文章图片地址
    front_image_path = scrapy.Field()
    #点赞数
    praise_nums = scrapy.Field()
    #收藏数
    bookmark_nums = scrapy.Field()
