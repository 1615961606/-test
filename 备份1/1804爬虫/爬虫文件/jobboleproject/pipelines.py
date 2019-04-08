# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.contrib.pipeline.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
import os

#自定义图片下载管道
#一定要记住使用ImagesPipeline管道的时候，要安装pillow(pip3 install pillow)
#获取图片的存储文件路径
image_store = get_project_settings().get('IMAGES_STORE')
class JobboleImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        #获取图片地址,发起请求
        imageurl = item['coverImageUrl']
        yield scrapy.Request(imageurl)

    def item_completed(self, results, item, info):
        print(results)
        """-
        [(Ture|False,{'url':'图片地址','path':'本地存储路径','checksum':'一个串'}),(),()]
        """
        paths = [subdict['path'] for status,subdict in results if status]

        if not paths:
            #如果图片没有下载成功,丢弃
            raise DropItem('图片没有下载，成功')
        else:
            # item['localImagePath'] = image_store+'/'+paths[0]
            os.rename(image_store+'/'+paths[0],image_store+'/'+item['title']+'.jpg')
            item['localImagePath'] = image_store+'/'+item['title']+'.jpg'

        #将item传递给下一个管道
        return item


#本地文件存储
# class JobboleprojectPipeline(object):
#
#     def __init__(self):
#
#         self.file = open('data.json','a')
#
#     def process_item(self, item, spider):
#         # print(item)
#         # 可以在这里做数据持久化
#         # with open('data.json','a') as file:
#         #     json_data = json.dumps(dict(item),ensure_ascii=False)
#         #     file.write(json_data+'\n')
#
#         json_data = json.dumps(dict(item),ensure_ascii=False)
#         self.file.write(json_data+'\n')
#
#         #如果有多个管道文件,并且有优先级顺序
#         #一定要记住return item,否则下一个管道
#         #无法接受item
#         return item
#
#     def open_spider(self,spider):
#         """
#         可选方法，在爬虫开始执行的时候调用一次
#         """
#         print(spider.name,'爬虫开启')
#
#
#     def close_spider(self,spider):
#         """
#         可选方法,在爬虫结束的时候调用一次
#         """
#
#         self.file.close()
#
#         print(spider.name,'爬虫结束')

#将数据存储到mysql数据库(改进版)
# from scrapy.utils.project import get_project_settings
import pymysql
from jobboleproject.items import JobboleprojectItem

class JobboleprojectPipeline(object):

    def __init__(self,host,user,pwd,db):
        #创建mysql连接
        self.client = pymysql.Connect(host,user,pwd,db,charset='utf8')
        #创建游标
        self.cursor = self.client.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']
        return cls(host,user,pwd,db)

    def process_item(self,item,spider):
        """
    　　　在爬虫文件中yield的item　都会经过这个方法
        """
        # sql = """
        # INSERT INTO boledb(title,publishTime,tags,author,content,articleUrl,votenums,collectnums,commentnums,coverImageUrl,localImagePath)
        # VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        # """
        # data = dict(item)
        # self.cursor.execute(sql,(data['title'],data['publishTime'],...))

        # if isinstance(item,'JobboleprojectItem'):
        #     pass
        # elif isinstance(item,'xxxxxxxx'):
        #     pass

        data = dict(item)
        sql,parmars = item.insert_db_by_data(data)

        try:
            self.cursor.execute(sql,parmars)
            self.client.commit()
        except Exception as err:
            self.client.rollback()
            print(err)

        return item

    def close_spider(self,spider):

        self.cursor.close()
        self.client.close()


#将数据存储到mongo
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
