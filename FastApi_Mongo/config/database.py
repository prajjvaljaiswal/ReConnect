from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
print("Connected to MongoDB")

db = client.users

collection_name = db["userSessions"]