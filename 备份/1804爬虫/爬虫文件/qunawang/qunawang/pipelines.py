# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class QunawangPipeline(object):

    def __init__(self,host,port,dbname):
        #创建mongo的客户端连接
        self.client = pymongo.MongoClient(host,port)
        #获取数据库（切换到指定数据库）
        self.db = self.client[dbname]


    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        dbname = crawler.settings['MONGO_DB']

        return cls(host,port,dbname)

    def process_item(self, item, spider):

        # if item['tags'] == '周边游':
        #     col = self.db['all_r']
        #     col.insert(dict(item))
        #
        # elif item['tags'] == '国内游':
        #     col = self.db['all_i']
        #     col.insert(dict(item))
        #
        # elif item['tags'] == '境外游':
        #     col = self.db['all_o']
        #     col.insert(dict(item))

        # 方法二：将判断写到item里面
        #获取集合名称

        col_name = item.get_collection_name_by_data(dict(item))
        #获取数据库下的集合
        col = self.db[col_name]
        #王几何中插入数据
        col.insert(dict(item))

        return item


    def close_spider(self,spider):
        #关闭数据库连接
        self.client.close()
