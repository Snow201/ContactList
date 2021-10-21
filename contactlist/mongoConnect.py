import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['ex_db']
mycol = mydb['students']
mydict =[{'Name':'Alex','fav':'Pizza'},{'Name':'Shlomo','fav':'Apple'},{'Name':'Matan','fav':'nofav'}]
#x = mycol.insert_one(mydict)
x = mycol.insert_many(mydict)

print(myclient.list_database_names())
print(mydb.list_collection_names())

for x in mycol.find({},{'_id':0,'name':0}):
    print(x)
