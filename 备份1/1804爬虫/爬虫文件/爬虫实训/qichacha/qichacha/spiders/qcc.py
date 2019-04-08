# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from qichacha.items import QichachaClassfyItem,QichachaCompanyItem

class QccSpider(scrapy.Spider):
    name = 'qcc'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.qichacha.com/']
    """
    step:根据https://www.qichacha.com/找到分类的信息,存入数据库
    """

    def parse(self, response):

        print(response.status)

        classifies = response.xpath('//li[@class="area  text-center"]')

        for li in classifies:
            #分类的item
            classify_item = QichachaClassfyItem()
            #标题
            classify_item['classifyName'] = li.xpath('./a/text()').extract_first('')
            #分类id
            classify_item['sign'] = li.xpath('./a/@href').extract_first('').replace('/','')
            #获取每一分类下第一页的url地址
            #样例：https://www.qichacha.com/g_AH.html
            #first_page_url = response.urljoin(classify_item['sign']+".html")
            first_page_url = 'https://www.qichacha.com/'+ classify_item['sign'] + ".html"
            classify_item['firstUrl'] = first_page_url

            yield classify_item
            # print(classify_item)

            # yield scrapy.Request(
            #     url=first_page_url,
            #     meta={
            #         'classifyName':classify_item['classifyName'],
            #         'sign':classify_item['sign'],
            #     },
            #     callback=self.parse_company_list
            # )

        first_page_url = 'https://www.qichacha.com/g_BJ_1.html'
        yield scrapy.Request(
            url=first_page_url,
            meta={
                'classifyName':'北京',
                'sign':'g_BJ',
            },
            callback=self.parse_company_list
        )

    def parse_company_list(self,response):

        """
        获取每一个分类页码下的公司的详情地址和标题
        :param response: 请求的响应结果
        :return:
        """
        print('列表状态码：', response.status)

        company_list = response.xpath('//section[@id="searchlist"]')

        if len(company_list) > 0:

            for section in company_list:
                #提取标题
                title = ''.join(section.xpath('.//span[@class="name"]//text()').extract()).replace(' ','')
                #提取公司详情的连接
                detail_url = section.xpath('./a[@class="list-group-item clearfix"]/@href').extract_first('')
                #将不完整的url拼接完整
                detail_url = response.urljoin(detail_url)
                print('正在发起'+title+'请求',detail_url)

                yield scrapy.Request(
                    detail_url,
                    callback=self.parse_company_detail,
                    meta = response.meta,
                )

        # 这里最好是一页一页的提取：
        next_page = response.xpath(
            '//ul[@class="pagination pagination-md"]/li[@class="next"]/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, meta={'sign': response.meta['sign']})

        # step2.获取当前页面中其他分页地址(获取当前页面中的其他分页地址)
        # other_page = response.xpath('//ul[@class="pagination pagination-md"]/li/a/@href').extract()
        #
        # for pageurl in other_page:
        #     pageUrl = response.urljoin(pageurl)
        #
        #     yield scrapy.Request(pageUrl, callback=self.parse)

    def parse_company_detail(self,response):
        """
        解析公司详情的数据
        :param response: 公司详情的响应结果
        :return:
        """
        print('正在解析公司详情')
        #实例化一个QichachaCompanyItem对象
        company_item = QichachaCompanyItem()
        if "企查查" in response.text:
            # 公司所属的分类
            company_item['sign'] = response.meta['sign']
            # 公司名称
            company_item['companyName'] = response.xpath('//div[@class="row title jk-tip"]/h1/text()').extract_first('暂无')
            # 是否在业
            company_item['tags'] = ','.join(response.xpath('//div[@class="row tags"]/span/text()').extract())
            # 电话
            #先做一个判断是否存在电话号码
            if len(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[1]/span[@class="cvlu"]/span')) > 0:
                company_item['phonenum'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[1]/span[@class="cvlu"]/span/a/text()').extract_first('').replace(' ','').replace('\n','')
                # print(len(phonenum))
            else:
                company_item['phonenum'] = '暂无'
                # print(phonenum)
            # 官网
            if len(response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a')) > 0:
                company_item['website'] = response.xpath('//div[@class="content"]/div[@class="row"][1]/span[@class="cvlu "]/a[1]/text()').extract_first('')
            else:
                company_item['website'] = '暂无'
            # 邮箱
            if len(response.xpath('//div[@class="content"]/div[@class="row"][2]/span[1]/span[@class="cvlu"]/a')) > 0:
                company_item['email'] = response.xpath('//div[@class="content"]/div[@class="row"][2]/span[1]/span[@class="cvlu"]/a/text()').extract_first('').replace(' ','').replace('\n','')
            else:
                company_item['email'] = '暂无'
            # 浏览量
            company_item['watchnum'] = response.xpath('//div[@class="company-record"]/span[1]/text()').extract_first('').replace('浏览：','')
            # 法人代表
            company_item['lagal'] = response.xpath('//a[@class="bname"]/h2/text()').extract_first('').replace(' ','').replace('\n','')
            # 注册资本
            company_item['capital'] = response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[1]/td[2]/text()').extract_first('暂无').replace(' ','').replace('\n','')
            # 成立日期
            company_item['build_date'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[2]/td[4]/text()').extract()).replace('\n','').replace(' ','')
            # 公司地址
            company_item['address'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[10]/td[2]/text()').extract()).replace('\n','').replace(' ','')
            # 统一社会信用代码
            company_item['credit_code'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[4]/td[4]/text()').extract()).replace('\n','').replace(' ','')
            # 注册号
            company_item['regist_number'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[4]/td[2]/text()').extract()).replace('\n','').replace(' ','')
            # 公司类型
            company_item['company_type'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[5]/td[2]/text()').extract()).replace('\n','').replace(' ','')
            # 所属行业
            company_item['industry'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[5]/td[4]/text()').extract()).replace('\n','').replace(' ', '')
            # 登记机关
            company_item['registration_authority'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[6]/td[4]/text()').extract()).replace('\n','').replace(' ', '')
            # 营业期限
            company_item['business_term'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[9]/td[4]/text()').extract()).replace('\n','').replace(' ', '')
            # 人员规模
            company_item['person_number'] = ''.join(response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[9]/td[2]/text()').extract()).replace('\n','').replace(' ', '')
            # 经营范围
            company_item['scope'] = response.xpath('//section[@class="panel b-a base_info"]/table[2]//tr[last()]/td[2]/text()').extract_first('暂无').replace('\n','').replace(' ','')

            print(company_item)





