from pydantic import BaseModel

class DoctorCreate(BaseModel):
    name:str
    email:str
    password:str
    phone_no:str
    role:str
    address:str

class DoctorUpdate(BaseModel):
    phone_no:str
    address:str