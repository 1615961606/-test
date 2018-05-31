import mysqlHelper
helper = mysqlHelper.MysqlHelper('127.0.0.1','root','bc123','ku3')
helper.connect()
sql = 'selext * from students where id>1'
data = helper.fetchall(sql)
if data:
	for temp in data:
		print(temp)
else:
	print('没有数据')
helper.close()