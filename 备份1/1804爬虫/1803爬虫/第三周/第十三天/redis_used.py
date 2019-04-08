from redis import *
redis_cli = StrictRedis(host='192.168.43.39',port=6379,db=0)
def insert_data():
    try:
        result = redis_cli.set('python_use','交互')
        print(result)
    except Exception as e:
        print(e)
def get_data():
    try:
        result = redis_cli.get('python_use')
        print(result)
    except Exception as e:
        print(e)

def updata_data():
    try:
        result = redis_cli.set('python_use','hahaha')
        print(result)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    insert_data()