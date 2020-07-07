import pymongo

client = pymongo.MongoClient("Here will be the local\online link for DB")

database = client['pydb_local']

collection = database['employess'] 

item = collection.find()

for li in item:
    print(li)
























