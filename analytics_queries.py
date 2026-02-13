from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['analytics_db']
collection = db['sales']

# Total purchases amount
total_amount = 0
for doc in collection.find():
    for purchase in doc['purchases']:
        total_amount += purchase['amount']

print("Total Sales:", total_amount)

client.close()
