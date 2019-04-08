from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import json
import re
def download_page_data(page,):
    xx_url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20311838&count=15&category={}'.format(page)
    # print(xx_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Referer': 'https://xueqiu.com/',
        'Cookie': 'aliyungf_tc=AQAAAG17MXnpYggA5CFxJBHpe11+Aukf; xq_a_token=8bb19a6c97ce8d72f0be4bcd51c906d270351669; xq_a_token.sig=D4IqV9nRrz2tk-MvcHsG0JxH_Jg; xq_r_token=892351a6205473ee21f05d419e3d2833127e1b1f; xq_r_token.sig=_E0ixyb9ctAQc_TN-YXfd28l7HQ; _ga=GA1.2.580061595.1540200407; _gid=GA1.2.593263393.1540200407; u=431540200411903; device_id=f49cafc20cce4c06b7b0bebe373f2b4a; s=e811bdb2s9; __utma=1.580061595.1540200407.1540200458.1540200458.1; __utmc=1; __utmz=1.1540200458.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=1.1.10.1540200458; Hm_lvt_1db88642e346389874251b5a1eded6e3=1540200406,1540200462; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1540200743; _gat_gtag_UA_16079156_4=1'
    }
    response = requests.get(xx_url,headers=headers)
    # print(response.text)
    print('数据加入成功')
        #2.将获取到的页面源码数据，返回
        # return response.text,response.status_code

    content = response.text
    python_content = json.loads(content)
    xue_list = python_content['list']
        # print(xue_list)
    for i in xue_list:
        print(type(i['data']))
        data3 = i['data']
        column = i.get('column')

        data4 = json.loads(data3)
        # print(data4)
        title = data4.get('title')
        screen_name = data4.get('user').get('screen_name')
        description = data4.get('description')
        view_count = data4.get('view_count')
        profile_image_url = data4.get('user').get('profile_image_url')

        dict = {
            'title':title,
            'screen_name':screen_name,
            'column':column,
            'description':description,
            'view_count':view_count,
            'profile_image_url':profile_image_url
        }
        print(dict)


#     description
#     title
# screen_name
# column
#     profile_image_url
#     view_count
    # print(result)
    # print(result)
        # print(type(data1))
        # print(result)
        # print(type(data1))

        # tags = data['column']
        # desc = data['description']
        # img_url = data['profile_image_url']
        # author = data['screen_name']
        # reads = data['view_count']

        # dict = {
        #     'title':title,
        #     'tags':tags,
        #     'desc':desc,
        #     'img_url':img_url,
        #     'author':author,
        #     'reads':reads
        # }
        # print(type(datas))
def download_done(future):
    print(future.result)



if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(max_workers=5)
    lists = [-1,6,101,102,104,105,110,111,113,114]


    for page in lists:
        page
        handler = thread_pool.submit(download_page_data,page)
        handler.add_done_callback(download_done)

    thread_pool.shutdown() #->实际上调用了join()方法
    
    
    
    
    
    
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=20311838&count=15&category=-1'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=644368&count=15&category=6'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=192138&count=15&category=105'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=191927&count=15&category=111'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=191861&count=15&category=102'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=191990&count=15&category=104'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=192007&count=15&category=101'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=191820&count=15&category=113'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=191259&count=15&category=114'
    # url = 'https://xueqiu.com/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=190839&count=15&category=110'