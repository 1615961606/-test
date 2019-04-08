# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义字段
class QunawangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #其他提示信息
    otherInfo = scrapy.Field()
    #price（价格）
    price = scrapy.Field()
    #历史成交量
    historySole = scrapy.Field()
    #产品编号
    productId = scrapy.Field()
    #评论量
    comments = scrapy.Field()
    #行程路线
    lineInfo = scrapy.Field()
    #景点图片地址
    images = scrapy.Field()
    #分类的标记
    tags = scrapy.Field()


    def get_collection_name_by_data(self,dataDict):

        #集合名称
        col_name = ''
        if dataDict['tags'] == '周边游':
            col_name = 'all_r'
        elif dataDict['tags'] == '国内游':
            col_name = 'all_i'
        elif dataDict['tags'] == '境外游':
            col_name = 'all_o'

        return col_name








