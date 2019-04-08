# -*- coding: utf-8 -*-

# Scrapy settings for qichacha project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qichacha'

SPIDER_MODULES = ['qichacha.spiders']
NEWSPIDER_MODULE = 'qichacha.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'qichacha (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
  'cookie':'acw_tc=3c1cb09c15409682667032696e3977cfe9d753635f42e0ac99999fc67d; _uab_collina=154096827317555175990353; UM_distinctid=166c8ddd59166-0abf3ff29b1f45-1e2e130c-1fa400-166c8ddd5934c1; zg_did=%7B%22did%22%3A%20%22166c8ddd88a24d-0bf0dbe15e1415-1e2e130c-1fa400-166c8ddd88c51f%22%7D; saveFpTip=true; QCCSESSID=c1fc2lmjq91q0q6ud5btprvle1; hasShow=1; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1543112423,1543274782,1543317929,1543373115; CNZZDATA1254842228=996490895-1540965260-%7C1543373815; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201543373112735%2C%22updated%22%3A%201543374767138%2C%22info%22%3A%201543112422850%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.baidu.com%22%2C%22cuid%22%3A%20%224ecca93f3349b65947ff2c6d33503045%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1543374771',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'qichacha.middlewares.QichachaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'qichacha.middlewares.QichachaDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#激活管道
ITEM_PIPELINES = {
   'qichacha.pipelines.QichachaPipeline': 300,
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

#数据库信息配置
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = 'ljh1314'
MYSQL_DB = 'qcc1804'
MYSQL_CHARSET = 'utf8'
