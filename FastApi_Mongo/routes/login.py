from fastapi import APIRouter, Response
from models.user import User
from config.database import collection_name
# from bson import ObjectId
from schema.schemas import list_serial, individual_serial
from middlewares.auth import create_jwt_token
from pydantic import BaseModel

loginRouter = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@loginRouter.post("/signup")
async def signup(user: User):
    collection_name.insert_one(dict(user))
    return {"data": "User created successfully"}

@loginRouter.post("/login")
async def login(user: LoginRequest,response: Response):
    newUser = collection_name.find_one({"email": user.email, "password": user.password})
    if not newUser:
        return {"data": "user not found"}
    newUser["_id"] = str(newUser["_id"])
    token = await create_jwt_token(newUser)
    response.set_cookie("jwt", token)
    return {"data": "Login successful", "user": individual_serial(newUser)}

@loginRouter.get("/logout")
async def logout(response: Response):
    response.delete_cookie("jwt")
    return {"data": "Logout successful"}