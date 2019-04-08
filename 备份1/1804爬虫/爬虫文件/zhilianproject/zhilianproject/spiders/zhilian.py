# -*- coding: utf-8 -*-
import scrapy
import json
from zhilianproject.items import ZhilianprojectItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    #https://fe-api.zhaopin.com/c/i/sou?start=120
    # &pageSize=60&cityId=530&workExperience=-1
    # &education=-1&companyType=-1&
    # employmentType=-1&jobWelfareTag=-1
    # &kw=%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98
    # &kt=3&lastUrlQuery=%7B%22p%22:3,%22pageSize%22:%2260%22,%22jl%22:%22530%22,%22kw%22:%22%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98%22,%22kt%22:%223%22%7D
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98&kt=3&lastUrlQuery=%7B%22pageSize%22:%2260%22,%22jl%22:%22530%22,%22kw%22:%22%E4%BA%BA%E4%BA%8B%E4%B8%93%E5%91%98%22,%22kt%22:%223%22%7D']

    def parse(self, response):
        print(response.status)
        # print(response.text)
        data = json.loads(response.text)
        # print(type(data))
        jobList = data['data']['results']
        # print(len(jobList))
        for job in jobList:
            # jobname = scrapy.Field()
            # salary = scrapy.Field()
            # companyName = scrapy.Field()
            # adress = scrapy.Field()
            # workyear = scrapy.Field()
            # degree = scrapy.Field()
            # needpeople = scrapy.Field()
            # jobinfo = scrapy.Field()
            # companyUrl = scrapy.Field()
            # jobUrl = scrapy.Field()
            jobitem = ZhilianprojectItem()
            jobitem['jobname'] = job['jobName']
            jobitem['salary'] = job['salary']
            jobitem['companyName'] = job['company']['name']
            # jobitem['adress'] = job[]
            jobitem['degree'] = job['eduLevel']['name']
            jobitem['workyear'] = job['workingExp']['name']
            jobitem['companyUrl'] = job['company']['url']
            jobitem['jobUrl'] = job['positionURL']

            yield scrapy.Request(jobitem['jobUrl'],
                                 callback=self.parse_job_detail,
                                 meta={'item':jobitem}
                                 )

    def parse_job_detail(self,response):

        with open('page.html','w') as file:
            file.write(response.text)


        jobitem = response.meta['item']

        #获取职位地址
        jobitem['adress'] = response.xpath('//div[@class="terminalpage-main clearfix"]//h2/text()').extract_first()
        #获取职位需要的人数
        # needpeoples = response.xpath('//div[@class="info-three l"]/span[4]/text()').re('\d+')
        # if len(needpeoples) > 0:
        #     jobitem['needpeople'] = needpeoples[0]
        # else:
        #     jobitem['needpeople'] = 0

        needpeoples = response.xpath('//div[@class="terminal-ul clearfix"]/li[7]/text()').re('\d+')
        if len(needpeoples) > 0:
            jobitem['needpeople'] = needpeoples[0]
        else:
            jobitem['needpeople'] = 0

        #获取职位的info信息
        jobitem['jobinfo'] = ''.join(response.xpath('//div[@class="terminalpage-main clearfix"]//div[@class="tab-inner-cont"]//p/text()').extract()).replace('\n','')

        #获取公司信息
        yield scrapy.Request(jobitem['companyUrl'],callback=self.parse_company)
        print(jobitem)

        yield jobitem

    def parse_company(self,response):
        pass

