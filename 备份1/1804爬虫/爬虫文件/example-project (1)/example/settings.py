# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

#指定scrapy_redis的过滤器组件，不在使用scrapy框架默认的过滤器组件了
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#指点scrapy_redis的调度器组件，不再使用scrapy矿建默认的调度器组件了
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#设置为True表示允许暂停和恢复(会保持爬虫的爬取记录，下一次恢复后会接着之前的继续爬取)
SCHEDULER_PERSIST = True

#scrapy的三种request队列模式

#1.一般通常都是使用这种,是默认的队列模式,有自己的优先级顺序
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

#启用了队列的形式，先进先出（相当于堆的结构）
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

#相当于栈的结构，先进的后出
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

#默认激活了scrapy_redis.pipelines.RedisPipeline的管道文件
#将item数据往redis数据库中存储
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#打印日志的等级
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
#设置下载延时
DOWNLOAD_DELAY = 1

#指定redis的相关配置
#指定要存储的redisde 主机ip,
REDIS_HOST = '127.0.0.1'

#指定要存储的redis 的端口号
REDIS_PORT = 6379

