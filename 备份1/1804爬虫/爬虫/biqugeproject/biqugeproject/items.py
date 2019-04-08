# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    article_name = scrapy.Field()
    article_content = scrapy.Field()
    tags = scrapy.Field()

    def insert_db_by_data(self, subdict):
        sql, data = get_sql_parmase_by_dict(subdict,'biqu')

        return sql, data

def get_sql_parmase_by_dict(subdict,biqu):

    sql = """
                INSERT INTO %s(%s)
                VALUES (%s)
                """ % (biqu,','.join(subdict.keys()), ','.join(['%s'] * len(subdict)))

    data = [value for value, key in subdict.items()]
    print('插入成功')
    return sql,data