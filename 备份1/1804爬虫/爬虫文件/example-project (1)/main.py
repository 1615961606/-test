import sys,os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#
# execute(['scrapy','crawl','dmoz'])

#
# execute(['scrapy','crawl','mycrawler_redis'])


execute(['scrapy','crawl','myspider_redis'])