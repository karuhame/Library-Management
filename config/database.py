from pymongo import MongoClient
# Connect to MongoDB
try:
    uri = "mongodb://localhost:27017/mydb"
    client = MongoClient(uri)
    database = client.get_database()
    accounts_collection = database['accounts']
    print("DB Connect Success")
except Exception as e:
    print(f"DB Failed: {e}")