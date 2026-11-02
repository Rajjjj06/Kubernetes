from pymongo import MongoClient
from os import environ

MONGO_HOST = environ.get('MONGO_HOST', 'localhost')

client = MongoClient(MONGO_HOST, 27017)

db=client["python-full"]


coll = db["names"]

print("MongoDB server:", client.address)
print("MongoDB databases:", client.list_database_names())
print("MongoDB documents:", list(coll.find()))