import urllib.request as request
import urllib.parse as parse
import ssl
import re
import pymysql
import json


startpage = int(input('请输入起始页'))
endpage = int(input('请输入结束页'))
for i in range(startpage,endpage+1):
    
    url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=%E8%AF%B7%E8%BE%93%E5%85%A5%E5%85%B3%E9%94%AE%E8%AF%8D&start={}#a'.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

    }
    ssl_context = ssl._create_unverified_context()
    req = request.Request(url,headers=headers)
    response = request.urlopen(req,context=ssl_context)
    content = response.read().decode()
    # print(content)
    parrern = re.compile('<td.*?l square.*?<a.*?href="(.*?)">(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>')
    contentss = re.findall(parrern,content)
    # print(result)
    dict = {
        'contentss':contentss
    }
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='bc123', db='tengxun', charset="utf8")
    
        cursor = conn.cursor()
      
      # insert_sql = """
        #             INSERT INTO tx VALUES(%s)
        #             """%(dict[contents])
        # cursor.execute(insert_sql,dict[contents])
        count = cursor.execute('insert into tx(contents) values(%s)',[value for key,value in dict.items()])
        print('save to mysql',count)
        conn.commit()
        if i == endpage+1:
            cursor.close()
            conn.close()
    except Exception as e:
        print(e)

    # dict = parse.urlencode(query=dict,encoding='utf8')
    # with open('tx'+str(i)+'.json','a') as f:
    #     f.write(json.dumps(dict,ensure_ascii=False)+'/n')
# save_to_mysql(dict)
# print(dict)

