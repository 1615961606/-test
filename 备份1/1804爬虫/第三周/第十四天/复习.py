通用爬虫：为了全站爬取
scrapy genspider -t crawl 爬虫名称 域名

rules规则属性的参数：是一个元组，可以放多个对象

创建rule：
linkextractor:设定提起规则
allow:要提取的正则
deny：不提取的正则
allow_domea:允许爬取的域
deny_dimea:不允许爬取的
restract_xpath:定位爬取的位置

注意：
1.设置回调的时候一定不能重写parse方法
2.要获取起始url的响应,必须重写parse_start_url
3.如果在设置rules规则的时候，如果没有callback回调函数，默认表示跟进

callback：设置回调函数
follow：是否跟进
process_links:设置一个函数,根据正则规则获取的url,可以在回调函数中获得

process_request:设置一个函数,可以在这个回调方法中拦截所有
根据正则提取的url构建的对象

什么情况用到通用爬虫？？
当我们提取数据的网站的网址很有规律，并且各个模块很清晰，我们就可以使用通用爬虫。