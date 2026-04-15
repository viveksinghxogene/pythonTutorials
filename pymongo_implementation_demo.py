from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
print('Database Created')

collection = database['product']
print('Collection Created')

products = [
    {
        "name": "IPhone",
        "price": 1000
    },
    {
        "name": "Mac Book",
        "price": 2000
    },
    {
        "name": "Dell",
        "price": 1500
    }
]