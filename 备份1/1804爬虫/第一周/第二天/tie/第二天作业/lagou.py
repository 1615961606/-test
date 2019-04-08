import requests
import re
import json
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='

}
form_data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python',
}
response = requests.get(url,headers=headers,params=form_data)
content = response.content.decode()
contents = json.loads(content)
print(type(contents))
for i in range(0,15):
    companyId = contents['content']['positionResult']['result'][i]['companyId']
    positionName = contents['content']['positionResult']['result'][i]['positionName']
    workYear = contents['content']['positionResult']['result'][i]['workYear']
    education = contents['content']['positionResult']['result'][i]['education']
    jobNature = contents['content']['positionResult']['result'][i]['jobNature']
    # print(len(positionName))
    dict = {
        'companyId':companyId,
        'positionName':positionName,
        'workYear':workYear,
        'education':education,
        'jobNature':jobNature
    }
    # print(dict)

    with open('lagou_data.json','a') as f:
        f.write(json.dumps(dict,ensure_ascii=False)+'\n')