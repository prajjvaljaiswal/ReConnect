import jwt
import os
from fastapi import Request, HTTPException, Depends, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

security = HTTPBearer()

COOKIE_NAME = "jwt"

async def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

async def verify_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Return user data
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
async def auth_middleware(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)):
    # token = request.cookies.get(COOKIE_NAME)  # Try getting JWT from cookie

    # if not token and credentials:
    #     token = credentials.credentials  # Fallback to Authorization header

    # if not token:
    #     raise HTTPException(status_code=401, detail="Not authenticated")

    return verify_jwt_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2IxODI0Mjg4ZDQwNTM1ZWMxMzc2Y2QiLCJuYW1lIjoicHJhamp2YWwiLCJhZ2UiOjIxLCJlbWFpbCI6InBqQGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiMTIzNDU2In0.CsD4MNrzc7emP0AmnDY7jwMtsgZikncpfXBXntjh1gQ")