from fastapi import APIRouter, Depends
from models.user import User
from config.database import collection_name
from bson import ObjectId
from schema.schemas import list_serial, individual_serial
from middlewares.auth import auth_middleware


testRouter = APIRouter()



@testRouter.get("/users")
async def get_users():
    users = list_serial(collection_name.find())
    return {"data": users}    

@testRouter.post("/users")
async def create_user(user: User):
    collection_name.insert_one(dict(user))
    return {"data": "User created successfully"}

@testRouter.get("/data")
async def get_data(user: dict = Depends(auth_middleware)):
    return {"data": "Data fetched successfully", "user": user}

@testRouter.get("/users/{email}")
async def get_user(email: str):
    user = individual_serial(collection_name.find_one({"email": email}))
    return {"data": user}

@testRouter.put("/users/{id}")
async def update_user(id: str, user: User):
    collection_name.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
    return {"data": "User updated successfully"}