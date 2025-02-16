from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
    password: str

    class Config:
        from_attributes = True