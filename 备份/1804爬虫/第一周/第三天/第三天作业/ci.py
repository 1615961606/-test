import urllib.request as request
import random
from urllib import error
import requests
import re
import time
import json
import pymysql
mysql_conn = pymysql.Connect('127.0.0.1','root','bc123','xici',port=3306,charset='utf8')
cursor = mysql_conn.cursor()
for i in range(1,50):
    # print(i)
    url = 'http://www.xicidaili.com/nn/{}'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }
    response = requests.get(url,headers=headers)
    content = response.content.decode()
    # print(content)
    parrern = re.compile('country.*?<img.*?>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<a.*?>(.*?)</a>',re.S)
    all_xi_url = re.findall(parrern,content)
    # print(all_xi_url) 

    proxy_lists = []

    # print('haha')
    # print(proxy_listy)
  
    for p in all_xi_url:
        proxy_lists.append(p[0]+':'+p[1])
        # print(proxy_lists)
    for uuu in proxy_lists:
        # print(uuu)
        proxy_list = [
            {"http":uuu},
        ]
        # print(proxy_list)
    # for i in proxy_list:
        prxoy = random.choice(proxy_list)
        httpproxy_handler = request.ProxyHandler(prxoy)

        opener = request.build_opener(httpproxy_handler)
        req = request.Request('http://httpbin.org/get')

        try:
            response = opener.open(req,timeout=3)
        except error.HTTPError as err:
            print(err.code)
            print(err.reason)
        except error.URLError as err:
            print(err.reason)
        else:
            dict = {
                'http':str(prxoy)
            }
            # dict['http'] = prxoy
            # ci_dict.append(prxoy)
            print('请求成功')
            print(dict)
            # with open('daili_su.json','a') as f:
            #     f.write(json.dumps(ci_dict,ensure_ascii=False)+'\n')
            
            sql = """
            INSERT INTO all_ip(%s) VALUES(%s)
            """%(','.join(dict.keys()),','.join(['%s']*len(dict)))
            try:
                cursor.execute(sql,[value for key,value in dict.items()])
                mysql_conn.commit()
                print('写入成功')
            except Exception as err:
                print(err)
                mysql_conn.rollback()