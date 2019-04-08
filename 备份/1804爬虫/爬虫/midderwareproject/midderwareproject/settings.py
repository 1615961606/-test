# -*- coding: utf-8 -*-

# Scrapy settings for midderwareproject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'midderwareproject'

SPIDER_MODULES = ['midderwareproject.spiders']
NEWSPIDER_MODULE = 'midderwareproject.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'midderwareproject (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#能处理的最大的并发请求数量
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载延迟的秒数
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#每个域名下最大的并发请求数量
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#限制并发ip的数量
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#是否要携带ip
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#通过telnet可以监听当前爬虫的状态，信息
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#设置默认的请求头
DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'midderwareproject.middlewares.MidderwareprojectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#中间件，一般自定义下载中间件，数字越小优先级越高
#DOWNLOADER_MIDDLEWARES = {
#    'midderwareproject.middlewares.MidderwareprojectDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#自定义扩展
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#设置并激活管道
ITEM_PIPELINES = {
   'midderwareproject.pipelines.MidderwareprojectPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#是否使用下载延迟
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#高延迟下的最大的下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#发送到每个服务器的并行请求数量
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#启用debug模式，只是接收到的每个response，可以通过此来查看限速参数是如何实时被调整的
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#是否启用缓存策略
#HTTPCACHE_ENABLED = True
#缓存超时时间
#HTTPCACHE_EXPIRATION_SECS = 0
#缓存保存路径
#HTTPCACHE_DIR = 'httpcache'
#缓存忽略的http状态玛
#HTTPCACHE_IGNORE_HTTP_CODES = []
#缓存存储的插件
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXIES = [
    {'ip_port':'113.128.148.31:8118','pwd_use':None},
    {'ip_port': '113.16.160.101:8118','pwd_use':None},
    {'ip_port': '111.197.238.158:8118','pwd_use':None},
    {'ip_port': '1.198.13.237:8010','pwd_use':'ijh:123'},
]