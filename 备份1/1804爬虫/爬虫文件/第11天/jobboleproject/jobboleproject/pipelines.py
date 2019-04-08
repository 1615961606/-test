# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  json

class JobboleprojectPipeline(object):

    def __init__(self):

        self.file = open('data.json','a')

    def process_item(self, item, spider):
        # print(item)
        # 可以在这里做数据持久化
        # with open('data.json','a') as file:
        #     json_data = json.dumps(dict(item),ensure_ascii=False)
        #     file.write(json_data+'\n')

        json_data = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(json_data+'\n')

        #如果有多个管道文件,并且有优先级顺序
        #一定要记住return item,否则下一个管道
        #无法接受item
        return item

    def open_spider(self,spider):
        """
        可选方法，在爬虫开始执行的时候调用一次
        """
        print(spider.name,'爬虫开启')


    def close_spider(self,spider):
        """
        可选方法,在爬虫结束的时候调用一次
        """

        self.file.close()

        print(spider.name,'爬虫结束')


class JobboleprojectPipelinetwo(object):

    def process_item(self, item, spider):
        # print(item)

        return item
