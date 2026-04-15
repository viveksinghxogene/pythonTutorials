from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
collection = database['product']

filter = {"name": "Dell"}
collection.update_one(filter, {"$set": {"price": 1800}})

cursor = collection.find({"name": "Dell"})
for eac_doc in cursor:
    print(eac_doc) 