from bs4 import BeautifulSoup
import requests
def qc_ceping():
    url = 'https://www.autohome.com.cn/bestauto/1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    content = response.text
    soup = BeautifulSoup(response.text,features='html.parser')
    che_even = soup.find_all(name='div',attrs={'class':'row'})
    for i in che_even:
        title = i.select('.picbox a img')
        if title == []:
            title = '未知'
        else:
            title = i.select('.picbox a img')[0].attrs['src']
        chengji1 = i.select('.dd-div1')
        if chengji1 == []:
            chengji1 = '未知'
        else:
            chengji1 = i.select('.dd-div2')[0].get_text()
        chengji2 = i.select('.dd-div1')
        if chengji2 == []:
            chengji2 = '未知'
        else:
            chengji2 = i.select('.dd-div2')[1].get_text()
     
        paiming = i.select('.dd-div3') 
        if paiming == []:
            paiming = '未知'
        else:
            paiming = i.select('.dd-div3 a')[0].get_text()
        num = i.select('.dd-div3 a')
        if num == []:
            num = '未知'
        else:
            num = i.select('.dd-div3 a')[0].get_text()
        xm = i.select('.dd-div1')
        if xm == []:
            xm = '未知'
        else:
            xm = i.select('.dd-div1')[0].get_text()
        xm1 = i.select('.dd-div1')
        if xm1 == []:
            xm1 = '未知'
        else:
            xm = i.select('.dd-div1')[1].get_text()
        xm2 = i.select('.dd-div1')
        if xm2 == []:
            xm2 = '未知'
        else:
            xm2 = i.select('.dd-div1')[2].get_text()

        bianji = i.select('.fn-clear dd .dd-div1')
        if bianji == []:
            bianji = '未知'
        else:
            bianji = i.select('.fn-clear dd .dd-div1 a')[0].get_text().replace(' ','').replace('\n','')
        bianji2 = i.select('.fn-clear dd .dd-div1')
        if bianji2 == []:
            bianji2 = '未知'
        else:
            bianji2 = i.select('.fn-clear dd .dd-div1 a')[1].get_text().replace(' ','').replace('\n','')
        bianji3 = i.select('.fn-clear dd .dd-div1')
        if bianji3 == []:
            bianji3 = '未知'
        else:
            bianji3 = i.select('.fn-clear dd .dd-div1 a')[2].get_text().replace(' ','').replace('\n','')

        dianping = i.select('.fn-clear dd .dd-div3')
        if dianping == []:
            dianping = '未知'
        else:
            dianping = i.select('.fn-clear dd .dd-div3 div.dd-div3-pp')[0].get_text().replace(' ','').replace('\n','')
            dianping1 = i.select('.fn-clear dd .dd-div3 div.dd-div3-pp')[1].get_text().replace(' ','').replace('\n','')
            dianping2 = i.select('.fn-clear dd .dd-div3 div.dd-div3-pp')[2].get_text().replace(' ','').replace('\n','')
            # print(dianping1)
            dict = {
            'title':title,
            'chengji':chengji1,
            'xm':xm,
            'dianping':dianping,
            'dianping1':dianping1,
            'dianping2':dianping2,
            'bianji':bianji,
            'bianji2':bianji,
            'bianji3':bianji,
        }
            print(dict)
    # for i in result:
    #     title = i.select('.dt-div2')
    #     print(title)
if __name__ == '__main__':
    qc_ceping()