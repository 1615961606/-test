# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jishi4project.spiders import cha
import pymongo
class Jishi4ProjectPipeline(object):

    def __init__(self,host,port,dbname):
        self.client = pymongo.MongoClient(host,port)
        self.db = self.client[dbname]

    @classmethod
    def from_crawler(cls,crawler):
        host = crawler.settings['MONGO_HOST']
        port = crawler.settings['MONGO_PORT']
        dbname = crawler.settings['MONGO_DB']
        return cls(host, port, dbname)


    def process_item(self, item, spider):

        col = self.db['paihang']
        col.insert(dict(item))
        print('插入成功')


        return item

    def close_spider(self):
        self.client.close()