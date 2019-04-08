# 列表，元素，集合，字典，字符串都是可迭代对象
data_list = [1,2,3,4,5,6,7]
for i in data_list:
    print(i)
# num = 10
data_lists = iter(data_list)
print(next(data_lists))
# from collections import Iterable
# print(isinstance(num,Iterable))