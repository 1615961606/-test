import pymongo

mongo_conn = pymongo.MongoClient(host='localhost',port=27017)

# class_1804db = mongo_conn('class_1804db')
class_1804db = mongo_conn.class_1804db

score = class_1804db['score']

def insert_data():
    document = {
        'name':'哈哈哈',
        'age':20,
        'score':'99'

    }
    result = score.insert(document)
    print(result)

if __name__ == '__main__':
    insert_data()