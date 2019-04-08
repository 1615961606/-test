import requests
from lxml import etree
def zhilian_project():
    url = 'https://www.zhaopin.com/'
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
    response = requests.get(url,headers=headers)
    content = response.text
    zhi_html = etree.HTML(content)
    get_title(zhi_html)

def get_title(content):
    title = content.xpath('//a[@class="zp-jobNavigater__pop--href"]/text()')
    for i in title:
        next_page_herf = 'https://sou.zhaopin.com/?jl=653&kw={}&kt=3'.format(i)
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            }
        # print(next_page_herf)
        response = requests.get(next_page_herf,headers=headers)
        content = response.text
        # print(content)
        html = etree.HTML(content)
        next_page = html.xpath('//div[@class="contentpile__content__wrapper__item clearfix"]')
        print(next_page)

if __name__ == "__main__":
    zhilian_project()
  