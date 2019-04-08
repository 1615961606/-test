# 首先需要安装pymongo:pip3 install pymongo
import pymongo
from bson.objectid import ObjectId

#创建一个客户端连接
mongo_conn = pymongo.MongoClient(host='127.0.0.1',port=27017)
#方式2
# mongo_conn = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
#有账号密码存在的情况
# mongo_conn = pymongo.MongoClient('mongodb://username:password@127.0.0.1:27017/')

#切换到指定的数据库
class1804_db = mongo_conn['class1804db']
# class1804_db = mongo_conn.class1804db

#获取数据库下的集合
score = class1804_db['score']
# score = class1804_db.score

def insert_data():
    document = {
        'name':'李明瑞',
        'age':20,
        'score':'100',
    }
    document1 = {
        'name':'李明瑞1号',
        'age':20,
        'score':'90',
    }
    document2 = {
        'name':'李明瑞2号',
        'age':20,
        'score':'80',
    }

    # result = score.insert(document)
    # result = score.insert_one(document)
    # print(result)

    result = score.insert([document1,document2])
    # result = score.insert_many([document1,document2])
    print(result)

#删除
def delete_data():
    #单条删除
    result = score.delete_one({'name':'李明瑞'})
    # result =score.remove({'name':'李明瑞'},multi=False)
    print(result)

    #删除多条
    result = score.delete_many({'name':'李明瑞'})
    # result = score.remove({'name':'李明瑞'})
    print(result)

#改
def update_data():
    #局部更新
    # result = score.update(
    #     {'name':'李明瑞1号'},
    #     {'$set':{'score':100}}
    # )

    #全文档更新
    # result = score.update(
    #     {'name':'李明瑞1号'},
    #     {'name':'娄雪嫚','age':18,'score':99,'info':'1804一朵花'}
    # )
    # print(result)

    # result = score.update_many({条件},{要替换的文档内容})
    
    #使用save进行数据的跟新
    #ObjectId("5bd65c4511575e07b08d194b")
    result = score.save({'_id':ObjectId("5bd65c4511575e07b08d194b"),'name':'王保轩','gender':'男','score':86})
    print(result)

#查找
def find_data():
    #查找集合下的所有文档
    # result = score.find({})
    # print(result)
    # print([data for data in result])

    #根据条件查找
    # result = score.find({'name':'王保轩'})
    # print(result)
    # print([data for data in result])

    #查找１条数据
    # result = score.find_one({'name':'王保轩'})
    # print(result)

    #count(),limit(),sort(),skip()
    #返回集合下的文档数量
    result = score.find({}).count()
    print(result)

    #跳过第一条，返回后5条，并且按照年龄降序排列
    # result = score.find({}).skip(1).limit(5).sort('age',-1)
    # print([data for data in result])

    #查找出所有文档，先按照年龄降序，再按照分数升序排列
    result = score.find({}).sort('age',-1).sort('score',1)
    print([data for data in result])
    result = score.find({}).sort([('age',-1),('score',1)])
    print([data for data in result])

if __name__ == '__main__':
    # insert_data()
    # delete_data()
    # update_data()
    find_data()
