from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client['analytics_db']
collection = db['sales']

# Load JSON data
with open('data/semi_structured_data.json') as f:
    data = json.load(f)

# Insert into MongoDB
collection.insert_many(data)
print("Data inserted successfully!")

client.close()
