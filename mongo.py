import pymongo

client = pymongo.MongoClient(host = 'localhost', port = 27017)
db = client.bigData
collection = db.mine_test
student = {
    'id':'20170101',
    'name':'aaa',
    'age':22,
    'gender':'male',
    'school':'rentongkeji',
    'adress':'sanhe'
}
student1 = {
    'id':'20170102',
    'name':'jack',
    'age':20,
    'gender':'male',
    'school':'qixin',
     'adress':'beijing'
}
# 插入数据后返回一个_id属性来唯一标识.ObjectID类型的_id属性
# result = collection.insert(student)
# print(result)
# print(type(result))
# print('----------------')
r23 = collection.insert_one(student)

print(r23)
