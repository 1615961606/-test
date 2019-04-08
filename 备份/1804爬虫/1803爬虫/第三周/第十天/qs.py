import requests
import re
url = 'http://www.quanshuwang.com/list/1_2.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36'

}
response = requests.get(url,headers=headers)
content = response.content.decode('gbk')
# print(content)
parrern = re.compile('<li.*?c999.*?<a.*?href="(.*?)">',re.S)
result = re.findall(parrern,content)
# print(result)
for i in result:
    url2 = i
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36'

}
    response2 = requests.get(url2,headers=headers)
    content2 = response2.content.decode('gbk')
    print(content2)

