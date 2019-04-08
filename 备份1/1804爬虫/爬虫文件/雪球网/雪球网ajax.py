# 1.分析目标网站
# 头条
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=-1

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=20298065&count=15&category=-1

#直播
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=6

# #沪深
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=105

# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=178343&count=15&category=105

#房产
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=111

#港股
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=102

#基金
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=104

#美股
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=101

# 私募
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=113

#保险
# https://xueqiu.com/v4/statuses/public_timeline_by_category.json?
# since_id=-1&max_id=-1&count=10&category=110

#多进程来实现
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import requests
import json,os
import threading

#利用进程池下载数据
pool = ProcessPoolExecutor(4)

#利用线程池解析数据
threadPool = ThreadPoolExecutor(10)

#获取每一页的数据
def get_data_from_parmas(parmas):
    # parmas:参数,get请求后面拼接的参数，是一个字典类型
    # requests.get(url,parmas)
    print('开启下载进程'+str(os.getpid()))
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Referer':'https://xueqiu.com/',
        'Cookie':'_ga=GA1.2.2007234704.1537273099; device_id=a118f672b464105016a05eb75e12e7c1; _gid=GA1.2.1835902343.1540198896; aliyungf_tc=AQAAALVFcnJT0AQA0hBAfFE0sCZPx9IV; xq_a_token=8bb19a6c97ce8d72f0be4bcd51c906d270351669; xq_a_token.sig=D4IqV9nRrz2tk-MvcHsG0JxH_Jg; xq_r_token=892351a6205473ee21f05d419e3d2833127e1b1f; xq_r_token.sig=_E0ixyb9ctAQc_TN-YXfd28l7HQ; _gat_gtag_UA_16079156_4=1; u=891540270559503; Hm_lvt_1db88642e346389874251b5a1eded6e3=1540198897,1540270560; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1540270560',
    }
    response = requests.get('https://xueqiu.com/v4/statuses/public_timeline_by_category.json?',params=parmas,headers=headers)
    print(response.status_code) #打印结果状态
    # response.json() = > json.loads(response.text)
    # print(response.json())
    parmas['count'] = 15
    parmas['max_id'] = response.json()['next_max_id']
    #将要获取的下一页的链接的参数，和响应结果返回
    print('结束下载进程'+str(os.getpid()))
    return parmas,response.json(),response.url

#下载完成后的回调
def download_done(future):
    # print(future.result()[0])
    # print(future.result()[2])
    #添加下一页的下载任务，继续下载
    handler = pool.submit(get_data_from_parmas,future.result()[0])
    handler.add_done_callback(download_done)

    #将下载的响应结果给线程池做解析操作
    jsonData = future.result()[1]
    threadhandler = threadPool.submit(parse_data,jsonData)
    threadhandler.add_done_callback(done)
    
    # parse_data(jsonData)

#解析数据，
def parse_data(data):
    print('-------'+threading.currentThread().name+'正在解析数据')
    #解析数据
    print(type(data))
    #获取雪球网的列表数据
    article_list = data['list']

    for article in article_list:
        article_dict = {}
        #分类名称
        article_dict['column'] = article['column']
        #内容
        contentJson = json.loads(article['data'])
        #文章的id
        article_dict['articleid'] = contentJson['id']
        #文章的连接
        article_dict['url'] = contentJson['target']
        #文章的标题
        article_dict['title'] = '未发现标题'
        if 'title' in contentJson:
            article_dict['title'] = contentJson['title']
        #用户名
        article_dict['username'] = '未知'
        article_dict['profile_image_url'] = '未知'
        if 'user' in contentJson:
            article_dict['username'] = contentJson['user']['screen_name']
            article_dict['profile_image_url'] = contentJson['user']['profile_image_url']

        print(article_dict)

    return 'done'

#解析完成后的回调
def done(future):
    #处理解析之后的回调
    print(future.result()+'解析完成')

if __name__ == '__main__':
    #进程池
    print('开启主进程'+str(os.getpid))
    # since_id=-1&max_id=-1&count=10&category=113
    list = [
        {'since_id':-1,'max_id':-1,'count':10,'category':-1},#头条
        {'since_id':-1,'max_id':-1,'count':10,'category':6},#直播
        {'since_id':-1,'max_id':-1,'count':10,'category':105},#沪深
        {'since_id':-1,'max_id':-1,'count':10,'category':111},#房产
        {'since_id':-1,'max_id':-1,'count':10,'category':102},#港股
        {'since_id':-1,'max_id':-1,'count':10,'category':104},#基金
        {'since_id':-1,'max_id':-1,'count':10,'category':101},#美股
        {'since_id':-1,'max_id':-1,'count':10,'category':113},#私募
        {'since_id':-1,'max_id':-1,'count':10,'category':110},#保险
    ]

    for parmas in list:
        handler = pool.submit(get_data_from_parmas,parmas)
        handler.add_done_callback(download_done)

    # pool.shutdown(wait=True)
    print('主进程结束'+str(os.getpid))
