from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode = True

class Productos(BaseModel):
    marca: str
    descripcion:str
    precio: str

    class Config():
        orm_mode = True

class ShowProductos(BaseModel):
    records: List[Productos]


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
