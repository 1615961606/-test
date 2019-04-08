import pymongo
# 连接数据库
mongo_conn = pymongo.MongoClient(host='localhost',port=27017)
# mongo_con = pymongo.MongoClient('mongodb://user:pwd@localhost:27017/')

# 切换到指定数据库
db = mongo_conn.chen
student_col = db.students
# students_col = db['students']

def add_data_to_db():
    document1 = {
        'name':'西资源',
        'info':'好人'
    }

    document2 = {
        'name':'洋娃娃',
        'info':'好看'
    }
    
    document3 = {
        'name':'小丑人',
        'info':'有趣'
    }
    
    result = student_col.insert(document1)
    print(result)
def delete_data():
    #删除一条
    result = student_col.delete_one({})
    result = student_col.remove({'name':'西资源'},multi=False)
    print(result)
    #删除多条
    result = student_col.delete_many({})
    # result = student_col.remove({'name':'xiziyuan'})

def update_data():
    result = student_col.update({'name':'好人'},{'$set':{'name':'美女'}})
    print(result)
    #全文档更新只修改一条
    # result = use_col.update({'name':'liyong'},{'name':'美女'})
    # print(result)
    #更新超照到的全部结果修改多条
    # result = use_col.update_many({'name':'美女'},{'$set':{'name':'徐资源'}})
    # print(result)
    #　使用save做更新操作,全文档更新
    #注意：name 'ObjectId' is not defined,导入Bson模块下的objectid
    result = student_col.save({'_id':ObjectId("5b836b9711575e79be9af0c7"),'name':'帅哥'})
def find_data():
    result = student_col.find({'name':'好人'})
    print(result)
# delete_data()
# add_data_to_db()
# update_data()
find_data()
