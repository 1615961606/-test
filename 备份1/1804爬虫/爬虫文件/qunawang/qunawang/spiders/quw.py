# -*- coding: utf-8 -*-
import scrapy
import re,json
from scrapy.selector import Selector
from qunawang.items import QunawangItem

class QuwSpider(scrapy.Spider):
    name = 'quw'
    allowed_domains = ['qunar.com']

    #https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30
    #https://tuan.qunar.com/vc/index.php?category=all_r&limit=30%2C30
    #https://tuan.qunar.com/vc/index.php?category=all_r&limit=60%2C30

    #https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30
    #https://tuan.qunar.com/vc/index.php?category=all_i&limit=30%2C30
    #https://tuan.qunar.com/vc/index.php?category=all_i&limit=60%2C30

    #https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30
    #https://tuan.qunar.com/vc/index.php?category=all_o&limit=30%2C30
    #https://tuan.qunar.com/vc/index.php?category=all_o&limit=60%2C30


    start_urls = [
        'https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30',
        'https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30',
        'https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30',
    ]

    def parse(self, response):

        category = ''
        linkcategory = ''
        #解析数据
        if response.url.find('all_r') > 0:
            print('周边游')
            category = '周边游'
            lizi = '一个例子'
            linkcategory = 'all_r'
        elif response.url.find('all_i') > 0:
            print('国内游')
            category = '国内游'
            linkcategory = 'all_i'
        elif response.url.find('all_o') > 0:
            print('境外游')
            category = '境外游'
            linkcategory = 'all_o'

        # scenic_links = response.xpath('//ul[@class="cf"]/li/a/@href').extract()
        # print(scenic_links)
        #<script>pageLoader({"id":"tuan-list"....."});</script>

        pattern = re.compile('<script>pageLoader\(({"id":"tuan-list".*?)\);</script>',re.S)

        json_str = re.findall(pattern,response.text)[0]

        html_str = json.loads(json_str)['html']

        with open('pagedata.html','w') as file:
            file.write(html_str)

        select_obj = Selector(text=html_str)

        scenic_links = select_obj.xpath('//div[@id="list"]/ul[@class="cf"]/li/a[1]/@href').extract()

        print(scenic_links)

        for url in scenic_links:

            full_url = 'https:' + url

            yield scrapy.Request(full_url,callback=self.parse_data_url,meta={'category':category})

        #取出景点的详情地址
        # print(html_str)

        #构造下一页的url地址并且发起请求
        #https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30
        pattern = re.compile('\d+',re.S)

        current_limit = re.search(pattern,response.url).group()

        next_limit = int(current_limit) +30
        #方式一，拼接完整的url
        # next_url = 'https://tuan.qunar.com/vc/index.php?category=%slimit=%s%2C30' % (linkcategory,str(next_limit))

        #方式二,将url中的limit后面的数字替换
        pattern = re.compile('limit=\d+',re.S)
        next_url = re.sub(pattern,'limit='+str(next_limit),response.url)
        print('next_url',next_url)

        yield scrapy.Request(next_url,callback=self.parse)

    def parse_data_url(self,response):
        
        print(response.status)
        category = response.meta['category']

        # with open('detail.html','w') as file:
        #
        #     file.write(response.text)

        deatil_url = 'https:' + response.xpath('.').re("location.href = '(.*?)'")[0]
        print(deatil_url)

        yield scrapy.Request(deatil_url,callback=self.parse_detail_data,meta={'category':category})

    def parse_detail_data(self,response):

        print(response.status)
        print('获取到正真的数据了')
        # with open('pagedetail.html','w') as file:
        #     file.write(response.text)
        #
        item = QunawangItem()
        # 提取目标数据
        #获取分类
        item['tags'] = response.meta['category']
        # 标题
        item['title'] = ''.join(response.css('div.summary h1::text').extract()).replace(' ','').replace('\n','')
        # 其他提示信息
        item['otherInfo'] = ','.join(response.css('span.feature-value ::text').extract())
        # price（价格）
        item['price'] = response.css('#js-min-price ::text').re('\d+')[0]
        # 历史成交量
        item['historySole'] = '0'
        # 产品编号
        item['productId'] = response.xpath('//div[@class="summary"]/div[@class="order"]/ul/li[1]/span/text()').extract_first()
        # 评论量
        item['comments'] = '0'
        # 行程路线
        item['lineInfo'] = ','.join(response.xpath('//span[@class="basic-info"]/em//text()').extract()).replace(' ','').replace('\n','')
        # 景点图片地址
        item['images'] = response.css('li.js-thumbnial a img::attr(src)').extract()

        # print(item)

        #根据这个接口获取评论量和成交量
        #https://cxly1.package.qunar.com/user/detail/getStatistics.json?pId=4059071795
        #https://jlaa3.package.qunar.com/user/detail/getStatistics.json?pId=4220401141
        #https://cxly1.package.qunar.com/user/detail.jsp?id=4059071795&rttp=出境游&dep=5YyX5Lqs&arr=5pmu5ZCJ5bKbLOazsOWbvSznpZ7ku5nljYrlspss5pmu5ZCJ6ZWHLOeah%
        pattern = re.compile('(https.*?com)/.*?id=(\d+).*?',re.S)

        result = re.findall(pattern,response.url)

        print(result)

        full_url = result[0][0] + '/user/detail/getStatistics.json?pId=' + result[0][1]

        yield scrapy.Request(full_url,callback=self.parse_comments_sold_data,meta={'item':item})

    def parse_comments_sold_data(self,response):

        item = response.meta['item']

        data = json.loads(response.text)

        soldCountHistory = data['data']['soldCountHistory']
        totalRatings = data['data']['totalRatings']

        item['historySole'] = soldCountHistory
        item['comments'] = totalRatings

        print(item)

        # yield item



