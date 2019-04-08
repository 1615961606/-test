from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.link import Link
from example.items import QidianItem
import scrapy,json

#只是用到了Redis的去重和保存功能，并没有实现分布式
class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    allowed_domains = ['qidian.com']
    start_urls = [
        'https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1',
    ]

    rules = [
        # 匹配分页的url
        # https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=2
        # https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=3

        Rule(
            LinkExtractor(
                allow=r'.*?page=\d+',
                restrict_xpaths=('//ul[@class="lbf-pagination-item-list"]',)
            ),
             follow=False,
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

    #拦截url,自己可以做一些处理
    def parse_links(self,links):
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

    def parse_book_detail(self,response):
        print('解析获取的页面数据')
        item = QidianItem()

        item['title'] = response.xpath('//div[@class="book-info "]/h1/em/text()').extract_first()
        item['content'] = response.xpath('//p[@class="intro"]/text()').extract_first()
        chpaterDict = {}
        volumes = response.xpath('//div[@class="volume-wrap"]//div[@class="volume"]')
        for volume in volumes:
            isfree = volume.xpath('.//h3/span/text()').extract_first().replace(' ','')
            if isfree == '免费':
                chapaterList = volume.xpath('.//ul[@class="cf"]/li')
                for chapter in chapaterList:
                    chpaterName = chapter.xpath('./a[1]/text()').extract_first()
                    chpaterUrl = chapter.xpath('./a[1]/@href').extract_first()
                    chpaterDict[chpaterName] = chpaterUrl

                    yield scrapy.Request('https:'+chpaterUrl,callback=self.parse_chpater_detail)

        item['chpaters'] = json.dumps(chpaterDict,ensure_ascii=False)

        yield item

    def parse_chpater_detail(self,response):
        print(response.status)
        #在这里解析章节的详情信息
        pass









