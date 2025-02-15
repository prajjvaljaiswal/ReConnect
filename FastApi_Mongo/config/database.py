from pymongo import MongoClient

client = MongoClient("mongodb+srv://prajjaiswal158:9967138778@cluster0.9h3bd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.users

collection_name = db["userSessions"]