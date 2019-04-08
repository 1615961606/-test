from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider

from example.items import QidianItem

import scrapy,json

from scrapy.link import Link

class MyCrawler(RedisCrawlSpider):
    #爬虫文件中只有两个地方跟我们单机版爬虫不一样
    #1.继承的类不一样,分布式爬虫继承自:RedisCrawlSpider
    #2.少了一个start_urls参数,多了一个redis_key:根据这个key从redis数据库中获取
    #爬虫的起始任务

    """Spider that reads urls from redis queue (myspider:start_urls)."""
    #爬虫名称
    name = 'mycrawler_redis'
    #一般情况下直接指定要爬取的域
    allowed_domains = ['qidian.com']
    #????:根据redis_key,从redis数据库中,取出请求任务
    redis_key = 'mycrawler:start_urls'

    rules = [
        # 匹配分页的url
        # https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=2
        # https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=3

        Rule(
            LinkExtractor(
                allow=r'.*?page=\d+',
                restrict_xpaths=('//ul[@class="lbf-pagination-item-list"]',)
            ),
            follow=True,
        ),
        # 用来匹配详情页的url地址
        # https://book.qidian.com/info/1009398284
        Rule(
            LinkExtractor(
                allow=r'.*?/info/\d+',
                restrict_xpaths=('//ul[@class="all-img-list cf"]',)
            ),
            callback='parse_book_detail',
            process_links='parse_links',
        ),
    ]

    #动态的获取要爬取的域，一般情况下不使用它，我们会使用allowed_domains
    #指定要爬取的域
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)

    #解析的回调方法，自己写
    # 拦截url,自己可以做一些处理
    def parse_links(self, links):
        """
        [
        Link(
        url='https://book.qidian.com/info/1004608738',
        text='',
        fragment='',
        nofollow=False),
        ....,
        ....
        ]

        """
        for sublink in links:
            sublink.url = sublink.url + '#Catalog'
        print(links)
        return links

    def parse_book_detail(self, response):
        print('解析获取的页面数据')
        item = QidianItem()

        item['title'] = response.xpath('//div[@class="book-info "]/h1/em/text()').extract_first()
        item['content'] = response.xpath('//p[@class="intro"]/text()').extract_first()
        chpaterDict = {}
        volumes = response.xpath('//div[@class="volume-wrap"]//div[@class="volume"]')
        for volume in volumes:
            isfree = volume.xpath('.//h3/span/text()').extract_first().replace(' ', '')
            if isfree == '免费':
                chapaterList = volume.xpath('.//ul[@class="cf"]/li')
                for chapter in chapaterList:
                    chpaterName = chapter.xpath('./a[1]/text()').extract_first()
                    chpaterUrl = chapter.xpath('./a[1]/@href').extract_first()
                    chpaterDict[chpaterName] = chpaterUrl

                    yield scrapy.Request('https:'+chpaterUrl, callback=self.parse_chpater_detail)

        item['chpaters'] = json.dumps(chpaterDict, ensure_ascii=False)

        yield item

    def parse_chpater_detail(self, response):
        print(response.status)
        # 在这里解析章节的详情信息
        pass