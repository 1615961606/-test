# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  pymysql

class QichachaPipeline(object):

    def __init__(self,host,user,pwd,db,charset):
        self.client = pymysql.Connect(host,user,pwd,db,charset=charset)
        self.cursor = self.client.cursor()

    def start_spider(self,spider):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        '''
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PWD = 'ljh1314'
        MYSQL_DB = 'qcc1804'
        MYSQL_CHARSET = 'utf8'
        :param crawler:
        :return:
        '''
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db  = crawler.settings['MYSQL_DB']
        charset = crawler.settings['MYSQL_CHARSET']

        return cls(host,user,pwd,db,charset)

    def process_item(self, item, spider):


        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.client.close()
