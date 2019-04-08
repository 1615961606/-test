import requests
import re
import pymysql

mysql_conn = pymysql.Connect('127.0.0.1','root','bc123','maoyan',port=3306,charset='utf8')
cursor = mysql_conn.cursor()
def mao_yan():
    for page in range(1,20):
        m_url = 'http://maoyan.com/cinemas?offset={}'.format(page*12)
        get_page(m_url)

def get_page(m_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    response = requests.get(m_url,headers=headers)
    content = response.content.decode()
    # print(content)
    get_data(content)
def get_data(content):
    parrern = re.compile('cinema-info.*?<a.*?href="(.*?)"+>(.*?</a>+.*?>(.*?)</p>)',re.S)
    mao_url = re.findall(parrern,content)
    # print(mao_url) 
    # print(content)
    for m in mao_url:
        my_url = m[0]
        my_name = m[1]
        my_adress = m[2]

        dict = {
            'my_url':my_url,
            'my_name':my_name,
            'my_adress':my_adress
        }
        # print(dict)
        write_data_db(dict)
def write_data_db(dict):
    sql = """
    INSERT INTO mao_yan(%s) VALUES(%s)
    """%(','.join(dict.keys()),','.join(['%s']*len(dict)))
    try:
        cursor.execute(sql,[value for key,value in dict.items()])
        mysql_conn.commit()
        print('写入成功')
    except Exception as err:
        print(err)
        mysql_conn.rollback()
def main():
    mao_yan()

if __name__ == '__main__':
    main()