# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# sys.setdefaultencoding('utf-8')
import pymongo
class BiqugeprojectPipeline(object):
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
        if item['tags'] == '玄幻小说':
            col = self.db['xuanhuan']
            col.insert(dict(item))
            print('玄幻小说插入成功')
        elif item['tags'] == '修真小说':
            col = self.db['xiuzhen']
            col.insert(dict(item))
            print('修真小说插入成功')

        elif item['tags'] == '都市小说':
            col = self.db['doushi']
            col.insert(dict(item))
            print('都市小说插入成功')

        elif item['tags'] == '穿越小说':
            col = self.db['chuanyue']
            col.insert(dict(item))
            print('穿越小说插入成功')

        elif item['tags'] == '网游小说':
            col = self.db['wangyou']
            col.insert(dict(item))
            print('网游小说插入成功')

        elif item['tags'] == '科幻小说':
            col = self.db['kehuan']
            col.insert(dict(item))
            print('科幻小说插入成功')

        return item

    def close_spider(self):
        self.client.close()