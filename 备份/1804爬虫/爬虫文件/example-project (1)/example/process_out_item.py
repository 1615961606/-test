#将数据导入mongodb
import redis
import pymysql
import pymongo
import json


def save_data_to_mongodb():
    #创建一个redis数据库的连接
    redisCli = redis.StrictRedis(host='localhost',port=6379)
    #创建一个mongodb的数据库连接
    mongoCli = pymongo.MongoClient(host='localhost',port=27017)
    #获取mongodb的数据库
    db = mongoCli['qidian']
    col = db['qd']

    #从redis数据库中取出数据
    while True:

        source,data  = redisCli.blpop('mycrawler_redis:items')
        #注意这里取出来的data是一个二进制数据的字符串
        str_data = data.decode('utf8')
        #得到一个json字符串,使用json.loads()转换为python数据类型
        itemData = json.loads(str_data)

        #将数据存入mongodb
        col.insert(itemData)


def save_data_to_mysql():
    #自己补充
    pass










if __name__ == '__main__':
    save_data_to_mongodb()

