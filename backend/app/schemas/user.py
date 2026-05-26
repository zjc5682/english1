#1.创建app/schemas/user.py
from pydantic import BaseModel,EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserRead(BaseModel):
    id:int 
    username:str
    email:str
    is_active:bool

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token:str
    token_type:str = "bearer"

class TokenData(BaseModel):
    username:Optional[str] = None

