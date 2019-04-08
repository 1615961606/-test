import csv
#写入列表类型的数据
with open("test.csv","w") as csvfile:
    #创建一个句柄
    write = csv.writer(csvfile)
    #往csv里面写入数据写入headersline的操作
    write.writerow(["name","age","gender"])
    #添加数据 writerow添加单行 writerows添加多行
    write.writerows([[0,1,2],[4,5,6],[7,8,9]])

#写入字典类型的数据
with open('text.csv',"w") as csvfile:
    fieldnames = ['index','a_name','b_name']
    #创建一个句柄
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    #写入头部
    writer.writeheader()
    #插入单个数据
    writer.writerow(
        {'index':'1','a_name':'2','b_name':'3'}
        )
    #插入多个数据
    write.writerows(
                {'index':'1','a_name':'2','b_name':'3'},
                {'index':'1','a_name':'2','b_name':'3'},
                {'index':'1','a_name':'2','b_name':'3'}



    )
#读取csv文件内容
import csv

with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(line)