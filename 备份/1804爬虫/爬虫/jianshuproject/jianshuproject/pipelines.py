# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class JianshuprojectPipeline(object):
    def __init__(self, host, port, dbname):
        # 创建mongo的客户端连接
        self.client = pymongo.MongoClient(host, port)
        # 获取数据库（切换到指定数据库）
        self.db = self.client[dbname]

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        dbname = crawler.settings['MONGO_DB']
        return cls(host,port,dbname)

    def process_item(self, item, spider):
        if item['tags'] == '故事':
            col = self.db['gushi']
            col.insert(dict(item))
            print('故事插入成功')
        elif item['tags'] == '读书':
            col = self.db['dushu']
            col.insert(dict(item))
            print('读书插入成功')

        elif item['tags'] == '旅行':
            col = self.db['lvxing']
            col.insert(dict(item))
            print('旅行插入成功')

        elif item['tags'] == '摄影':
            col = self.db['sheying']
            col.insert(dict(item))
            print('摄影插入成功')

        return item

    def close_spider(self):
        self.client.close()