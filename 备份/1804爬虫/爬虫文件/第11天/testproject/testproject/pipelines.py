# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#管道文件,一般在这里做数据过滤，和持久化
class TestprojectPipeline(object):
    def process_item(self, item, spider):
        return item
