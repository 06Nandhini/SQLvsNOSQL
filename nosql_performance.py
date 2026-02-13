from pymongo import MongoClient
import time

client = MongoClient("mongodb://localhost:27017/")
db = client['analytics_db']
collection = db['sales']

# Count documents with high-value purchases
start = time.time()
count = collection.count_documents({"purchases.amount": {"$gt": 1000}})
end = time.time()

print("High-value purchases:", count)
print("Execution Time:", end - start, "seconds")

client.close()
