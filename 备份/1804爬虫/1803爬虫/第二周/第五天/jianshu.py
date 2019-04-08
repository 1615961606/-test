import requests
import re
import urllib.parse as parse
import json
url = 'https://www.jianshu.com/c/7b2be866f564?utm_medium=index-collections&utm_source=desktop'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36'

}
response = requests.get(url,headers=headers)
content = response.content.decode()
# print(content)
# print(responses.content.decode())
parttern = re.compile('<li.*?wrap-img.*?href="(.*?)".*?<img.*?src="(.*?)".*?title.*?>(.*?</a>).*?>(.*?</p>)',re.S)

result = re.findall(parttern,content)
for i in result:

    http = i[0],
    images = i[1],
    title = i[2],
    con = i[3]
    responses = requests.get('https://upload-images.jianshu.io/upload_images/2634547-f68985c3b4f1cf1e.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240',headers=headers)
# print('https://www.jianshu.com'+http)
    # print(responses.content)
    with open('ok.jpg','wb+') as f:
        f.write(responses.content)
    dict = {
        'http':http,
        'images':images,
        'title':title,
        'con':con
    }
    # for key,value in dict.items():
    #     print(key,value)
    # print(str(dict['http']))
    with open('jian.json','a') as f:
        f.write(json.dumps(dict,ensure_ascii=False)+'\n')
# base_url = 'https://www.jianshu.com/p/0b6bc0355aa7'
# son_url = str(http)
# fullurl = parse.urljoin(base_url,son_url)
# print(fullurl)


 
