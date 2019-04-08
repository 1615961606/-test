# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from jishi4project.spiders import cha
from jishi4project.items import Jishi4ProjectItem
from  jishi4project.items import first_page_Item,Name_projectItem
import pymongo
import pymysql
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from jishi4project import items
class Jishi4ProjectPipeline(object):

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
        if isinstance(item,first_page_Item):
            sql = """
                    INSERT INTO shii(%s) VALUES(%s)
                    """ % (','.join(dict(item).keys()), ','.join(['%s'] * len(dict(item))))
            try:
                self.cursor.execute(sql, [value for key, value in dict(item).items()])
                self.client.commit()
                print('写入成功')
            except Exception as err:
                print(err)
                self.client.rollback()

            return item






