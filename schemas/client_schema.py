from pydantic import BaseModel

class ClientCreate(BaseModel):
    name:str
    email:str
    password:str
    phone_no:str
    address:str

class ClientUpdate(BaseModel):
    phone_no:str
    address:str