import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

database = client['pydb_local']

collection = database['employess'] 

item = collection.find()

for li in item:
    print(li)
























