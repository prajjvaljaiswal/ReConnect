from fastapi import APIRouter
from models.user import User
from config.database import collection_name
# from bson import ObjectId
from schema.schemas import list_serial

testRouter = APIRouter()

@testRouter.get("/users")
async def get_users():
    users = list_serial(collection_name.find())
    return {"data": users}    

@testRouter.post("/users")
async def create_user(user: User):
    collection_name.insert_one(dict(user))
    return {"data": "User created successfully"}