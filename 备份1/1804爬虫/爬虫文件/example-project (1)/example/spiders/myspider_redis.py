from scrapy_redis.spiders import RedisSpider
import scrapy,json
from example.items import QidianItem

class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    # 爬虫文件中只有两个地方跟我们单机版爬虫不一样
    # 1.继承的类不一样,分布式爬虫继承自:RedisSpider
    # 2.少了一个start_urls参数,多了一个redis_key:根据这个key从redis数据库中获取
    # 爬虫的起始任务
    #爬虫名称
    name = 'myspider_redis'
    #指定要爬取的域
    allowed_domains = ['qidian.com']
    #根据redis_key从redis数据库中取出起始任务
    redis_key = 'myspider:start_urls'

    # #动态获取要爬取的域,一般不用,我们直接使用allowed_domains指定要爬取的域
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        #stp1:获取小说的详情地址连接
        novals = response.xpath('//ul[@class="all-img-list cf"]/li')
        for noval in novals:

            noval_url = 'https:' + noval.xpath('./div[@class="book-mid-info"]/h4/a/@href').extract_first() +'#Catalog'

            yield scrapy.Request(noval_url,callback=self.parse_noval_detail)

        #step2:获取当前分页下的其他分页的连接
        other_page_urls = response.xpath('//ul[@class="lbf-pagination-item-list"]/li/a/@href').extract()

        for url in other_page_urls:
            if url.find('page') > 0:
                full_url = 'https:' + url
                yield scrapy.Request(full_url,callback=self.parse)

    def parse_noval_detail(self,response):

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

                    yield scrapy.Request('https:' + chpaterUrl, callback=self.parse_chpater_detail)

        item['chpaters'] = json.dumps(chpaterDict, ensure_ascii=False)

        yield item

    def parse_chpater_detail(self, response):
        print(response.status)
        # 在这里解析章节的详情信息
        pass
