# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jishi4project.spiders import cha
from jishi4project.items import Jishi4ProjectItem
from  jishi4project.items import first_page_Item
import pymongo
import pymysql
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from jishi4project import items
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
        if isinstance(item,Jishi4ProjectItem):
            col = self.db['paihang']
            col.insert(dict(item))
            print('插入成功')
        elif isinstance(item,first_page_Item):
            col = self.db['forst']
            col.insert(dict(item))
            print('哈哈哈哈啊哈')
            return item

    def close_spider(self):
        self.client.close()