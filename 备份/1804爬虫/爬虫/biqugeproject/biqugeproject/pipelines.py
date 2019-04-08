# -*- coding: utf-8 -*-
# FEED_EXPORT_ENCODING = 'utf-8'
#encoding:utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# sys.setdefaultencoding('utf-8')
import imp
import sys
imp.reload(sys)
import pymysql
# sys.setdefaultencoding( "utf-8" )
import pymongo
from biqugeproject.items import BiqugeprojectItem
class BiqugeprojectPipeline(object):
    def __init__(self, host, user, pwd, db):
        # 创建mysql连接
        self.client = pymysql.Connect(host, user, pwd, db, charset='utf8')
        # 创建游标
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        return cls(host, user, pwd, db)

    def process_item(self, item, spider):


        data = dict(item)
        sql, parmars = BiqugeprojectItem.insert_db_by_data(item,'biqu')

        try:
            self.cursor.execute(sql, parmars)
            self.client.commit()
        except Exception as err:
            self.client.rollback()
            print(err)

        return item

    def close_spider(self, spider):

        self.cursor.close()
        self.client.close()


# 将数据存储到mongo
# import  pymongo
# class JobboleprojectPipeline(object):
#
#     def __init__(self):
#         self.client = pymongo.MongoClient('127.0.0.1',27017)
#         #选择数据库
#         self.db = self.client['boledb']
#         #选择数据库下的集合
#         self.col = self.db['jobbole']
#
#     def process_item(self,item,spider):
#         #将数据存入集合
#         self.col.insert(dict(item))
#
#     def close_spider(self,spider):
#         self.client.close()

class JobboleprojectPipelinetwo(object):

    def process_item(self, item, spider):
        # print(item)

        return item





























    # def __init__(self,host,port,dbname):
    #     self.client = pymongo.MongoClient(host,port)
    #     self.db = self.client[dbname]
    #
    # @classmethod
    # def from_crawler(cls,crawler):
    #     host = crawler.settings['MONGO_HOST']
    #     port = crawler.settings['MONGO_PORT']
    #     dbname = crawler.settings['MONGO_DB']
    #     return cls(host, port, dbname)
    #
    #
    # def process_item(self, item, spider):
    #     if item['tags'] == '玄幻小说':
    #         col = self.db['xuanhuan']
    #         col.insert(dict(item))
    #         # print('玄幻小说插入成功')
    #     elif item['tags'] == '修真小说':
    #         col = self.db['xiuzhen']
    #         col.insert(dict(item))
    #         # print('修真小说插入成功')
    #
    #     elif item['tags'] == '都市小说':
    #         col = self.db['doushi']
    #         col.insert(dict(item))
    #         # print('都市小说插入成功')
    #
    #     elif item['tags'] == '穿越小说':
    #         col = self.db['chuanyue']
    #         col.insert(dict(item))
    #         # print('穿越小说插入成功')
    #
    #     elif item['tags'] == '网游小说':
    #         col = self.db['wangyou']
    #         col.insert(dict(item))
    #         # print('网游小说插入成功')
    #
    #     elif item['tags'] == '科幻小说':
    #         col = self.db['kehuan']
    #         col.insert(dict(item))
    #         print('科幻小说插入成功')

        # return item

    # def close_spider(self):
    #     self.client.close()