# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#自定义字段,为了后面赋值时使用(类似于model的作用)
class JobboleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #文章标题
    title = scrapy.Field()
    #发布时间
    publishTime = scrapy.Field()
    #标签
    tags = scrapy.Field()
    #作者
    author = scrapy.Field()
    #文章的内容
    content = scrapy.Field()
    #文章的地址
    articleUrl = scrapy.Field()
    #点赞量
    votenums = scrapy.Field()
    #收藏量
    collectnums = scrapy.Field()
    #评论量
    commentnums = scrapy.Field()
    #图片的url
    coverImageUrl = scrapy.Field()
    #本地图片的存储路径
    localImagePath = scrapy.Field()

    def insert_db_by_data(self,subdict):

        sql,data = get_sql_parmase_by_dict(subdict,'boledb')

        return sql,data



def get_sql_parmase_by_dict(subdict,tablename):

    sql = """
                INSERT INTO %s(%s)
                VALUES (%s)
                """ % (tablename,','.join(subdict.keys()), ','.join(['%s'] * len(subdict)))

    data = [value for value, key in subdict.items()]

    return sql,data




