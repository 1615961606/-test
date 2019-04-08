import requests
import urllib.parse as parse
import re
import json
import pymysql

mysql_conn = pymysql.Connect(
    '127.0.0.1','root','bc123','qidian_chen',port=3306,charset='utf8'
)
cursor = mysql_conn.cursor()
def qidian():
    url = 'https://www.qidian.com/free/all'
    
    write_data(url)
def write_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }
    response = requests.get(url,headers=headers)
    content = response.content.decode()
    all_data_get = re.compile('book-mid-info.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>.*?intro.*?>(.*?)</p>',re.S)
    all_data_get_image = re.compile('book-img-box.*?<img.*?src="(.*?)"',re.S)
    
    pattern = re.compile(
        '<li.*?lbf-pagination-item"><a\shref="(.*?)"',re.S
    )
    result = re.findall(pattern,content)
    naex_url = result[1]
    if naex_url is not 'javascript:;':
        naex_url = 'https:'+naex_url
    # print(next_page)
    all_data_image = re.findall(all_data_get_image,content)
    # print(all_data_image)
    all_data = re.findall(all_data_get,content)
    # print(all_data)
    content = content
    # print(all_data)
    for page in all_data:
        title = page[0]
        print(title)
        author = page[1]
        tag = page[2]+page[3]
        datas = page[4]
        dict = {
            'title':title,
            'author':author,
            'tag':tag,
            'datas':datas
        }
        print(dict)
        down_image(all_data_image,title)
        insert_data_to_db(dict)
    write_data(naex_url)
        # print(dict)
def down_image(all_data_image,title):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    }
    for img_url in all_data_image:
        good_url = 'https://bookcover.yuewen.com/qdbimg/349573/1009368407/150'
        img_url = parse.urljoin(good_url,img_url)
        response = requests.get(img_url,headers=headers)
        image_content = response.content
        # print(file_name)
        file_name = img_url[-7:-4]
        with open('qi_images/'+str(file_name)+'.jpg','wb+') as f:
            file_name = title
            f.write(image_content)      
def insert_data_to_db(subdict):
    sql = """
    INSERT INTO qidian(%s) VALUES(%s)
    """%(','.join(subdict.keys()),','.join(['%s']*len(subdict)))

    try:
        cursor.execute(sql,[value for key,value in subdict.items()])
        mysql_conn.commit()
        print('写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()
if __name__ == '__main__':
    qidian()