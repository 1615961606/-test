# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QichachaClassfyItem(scrapy.Item):
    #分类的字段
    #分类名称
    classifyName = scrapy.Field()
    #分类的表示
    sign = scrapy.Field()
    #首页列表地址
    firstUrl = scrapy.Field()

    def insert_sql_data_by_dictdata(self,dictdata):
        """
        step1:写一个数据插入的sql语句
        step2:数据库要存储的数据提取出来
        :param dictdata: 字典类型的数据
        :return:
        """
        sql = """
        INSERT INTO category (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s']*len(dictdata))
        )

        data = list(dictdata.values())
        # data = [value for key,value in dictdata.items()]

        return sql,data
    
class QichachaCompanyItem(scrapy.Item):
    """
    存储公司详情的信息
    """
    #公司所属的分类
    sign = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 是否在业
    tags = scrapy.Field()
    # 电话
    phonenum = scrapy.Field()
    # 官网
    website = scrapy.Field()
    # 邮箱
    email = scrapy.Field()
    #浏览量
    watchnum = scrapy.Field()
    # 法人代表
    lagal = scrapy.Field()
    # 注册资本
    capital = scrapy.Field()
    # 成立日期
    build_date = scrapy.Field()
    # 公司地址
    address = scrapy.Field()
    # 统一社会信用代码
    credit_code = scrapy.Field()
    # 注册号
    regist_number = scrapy.Field()
    # 人员规模
    person_number = scrapy.Field()
    # 公司类型
    company_type = scrapy.Field()
    # 登记机关
    registration_authority = scrapy.Field()
    # 营业期限
    business_term = scrapy.Field()
    # 所属行业
    industry = scrapy.Field()
    # 经营范围
    scope = scrapy.Field()

    def insert_sql_data_by_dictdata(self,dictdata):
        """
        step1:写一个数据插入的sql语句
        step2:数据库要存储的数据提取出来
        :param dictdata: 字典类型的数据
        :return:
        replace具备替换拥有唯一索引或者主键索引重复数据的能力，
        也就是如果使用replace into插入的数据的唯一索引或者主键
        索引与之前的数据有重复的情况，将会删除原先的数据，然后再
        进行添加
        REPLACE INTO users (id,name,age) VALUES(123, ‘chao’, 50);
        """
        sql = """
        INSERT INTO company (%s)
        VALUES (%s)
        """ % (
            ','.join(dictdata.keys()),
            ','.join(['%s']*len(dictdata))
        )

        data = list(dictdata.values())
        # data = [value for key,value in dictdata.items()]

        return sql,data






