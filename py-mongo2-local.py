
import pymongo

client = pymongo.MongoClient("Here will be the localDB link")

database = client['pydb_local']

collection = database['employess'] 

item = collection.find()

for li in item:
    print(li)

new_item = {
	"first_name": "mohamad",
	"last_name": "s",
	"email": "mohamad@yahoo.com",
	"job_title": "WD",
	"salary": 26000
}
###collection.insert_one(new_item)
# line above is commited to avoid adding repeating same data

item = collection.find()
for li in item:
    print(li)

new_items = [ 
    {"first_name" : "waheed", "last_name" : "amin" , "email" : "wa@yahoo.com", "job_title" : "HR", "salary": 22000},
    {"first_name" : "Rida", "last_name" : "jj" , "email" : "rida@gmail.com", "job_title" : "W Developer", "salary": 28000},
    {"first_name" : "Jalal", "last_name" : "Jalali" , "email" : "ja@yahoo.com", "job_title" : "game Developer", "salary": 29000}
     ]

collection.insert_many(new_items)

item = collection.find({})
for li in item:
     print(li)
         


