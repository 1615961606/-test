
data_dict = {
    'name':'ljh',
    'age':20
}

# sql = """
# INSERT INTO nametable(name,age)
# VALUES(%s,%s)
# """

print(
    ','.join(data_dict.keys())
    )
print(
    ','.join(['%s']*len(data_dict))
    )
