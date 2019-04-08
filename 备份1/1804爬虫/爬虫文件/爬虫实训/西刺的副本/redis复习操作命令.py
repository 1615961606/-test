1.启动
sudo redis-server /etc/redis/redis.conf
1.链接客户端
redis-cli

redis-cli -h ip地址 -p 端口号



#关于健的基本操作
#查看所有键
keys *
# 查看健的类型
type key

# 查看键书否存在
exists key
#删除健
del key

#关于字符串的操作
#插入键值
set key value
# 设置多个键值
mset key1 value key2 value2
#获得单个key
get key
#获得多个key
mget key1 key2
#给某一个键设置过期时间
setex key seconds(时间) value


#如果健不存在则创建,存在什么都不做
setnx key value


setrange key offset(偏移量) value (重偏移量位置修改)

#拼接
append key value



#删除
del key


#hash 值的操作
#单个
hset key field value
#多个
hmset key field1 value1 field2 value2
# 取值
获取hash值中所有的域 (健)
hkeys keyname
获取hash值中所有的域对应的值
#获得所有的值
hvals keyname
# 对应域下的值
hget keyname field
# 获取多个域下面的值
hmget keyname Field1 field2

#删除
hdel keyname field [field1,field2]

#关于list 操作起始是一个双向的列表
(重左边开始插入,先插入的在后面)
lpush keyname value value....
右边
rpush keyname value value value ....

#添加
linsert keyname before|after value(参照值) newvalue(要插入的数据)
#修改
lset keyname index newvalue
#查找
lrange keyname start(0) stop(-1)
#删除
lrem keyname count(count是有方向的正负,正前往后,负后往前,0全删) value 

关于set无序集合的操作
sadd keyname member1 member2 member3
获取集合下的所有成员
smembers keyname
#判断某个成员是否在集合下
sismember keyname member

#删除集合下的成员
srem keyname member1 member2...
#随机获取并删除
spop keyname count(要返回的数量)
#有序集合zset
#添加:score:表示权重
zadd keyname score member score member

#根据索引获取
zrange keyname start(0) stop(-1)

#根据权重获取
zrangebyscore keyname min  max


#获取某一个成员的权重
zscore keyname member


#删除
#删除指定成员

zrem keyname member member

zremrangebyscore key min max 根据权重范围删除成员



