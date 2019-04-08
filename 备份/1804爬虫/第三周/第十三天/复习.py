#图片下载
第一种：正常的发起请求，获取图片的二进制文件，保存。
第二种：自定义图片管道，继承ImagePipline
    重写两个方法


数据持久化(切记，激活管道)
    def __init__(self,xxx):
        可以设置一些参数（创建数据库连接，打开文件）

    @classmethed
    def from_crawler(cls,crawler):
        crawler:包含了爬虫的一些核心组件
        可以获取setting中设置的一些参数

        return cla(xx,xx)
     1 自定义数据管道
     def openspider(self,spider):
         可选方法,在爬虫开启的时候会调用
     def process_item(self,item,spider):
         #所有的item都会经过这个方法
        在这里做数据持久化
        if ininstance(item,类名)：
            做数据插入操作
        elif isinstance(item,类名):
            做数据插入操作

    #方法二
        1 在item对应的类，我们定义一个方法
        返回sql语句和要插入的语句
        2 使用item调用这个方法，得到sql语句和要插入的语句
        3.执行插入操作


        return item(如果要将item，传递给下一个管道，必须要rerurnitem)
     def close_spider(self,spider):
         关闭文件，在爬虫结束的时候会调用
         关闭数据库

scrapy shell 交互式终端的使用
scrapy shell链接


#scrapy spider

customer——settings：各爬虫文件可以根据这个参数做自定义的参数设置，会覆盖setting.py文件中设置的全局参数

def start_requests():
    #根据其实url，发起请求

def parse(self,response):
    得到响应的回调数据