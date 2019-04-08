# -*- coding: utf-8 -*-

# Scrapy settings for qunawang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qunawang'

SPIDER_MODULES = ['qunawang.spiders']
NEWSPIDER_MODULE = 'qunawang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qunawang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qunawang.middlewares.QunawangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'qunawang.middlewares.QunawangDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'qunawang.pipelines.QunawangPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline':400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#关于数据库的设置
#设置host
MONGO_HOST = 'localhost'
#设置端口
MONGO_PORT = 27017
#设置数据库名称
MONGO_DB = 'qunawang'



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


#打印日志的等级
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.

#指定redis的相关配置
#指定要存储的redisde 主机ip,
REDIS_HOST = '127.0.0.1'

#指定要存储的redis 的端口号
REDIS_PORT = 6379