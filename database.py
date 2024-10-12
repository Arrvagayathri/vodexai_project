from pymongo import MongoClient
import os

MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_DETAILS)
db = client["database1"]
items_collection = db["items"]
clock_in_collection = db["clock_in_records"]
