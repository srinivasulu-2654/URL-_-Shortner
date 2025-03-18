from pymongo import MongoClient
import os

# Get MongoDB connection string (or use local MongoDB)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)

# Select database and collection
db = client["url_shortener"]
urls_collection = db["urls"]
