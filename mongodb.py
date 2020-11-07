from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbgnsia

all_users = list(db.users.find({}))

same_ages = list(db.users.find({'age':33}))

db.users.delete_one({'name':'joonse'})

user = db.users.find_one({'name':'joonse'},{'_id':False})
print(user)
