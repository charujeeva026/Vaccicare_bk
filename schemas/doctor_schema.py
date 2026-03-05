from pydantic import BaseModel,EmailStr

class DoctorCreate(BaseModel):
    name:str
    email:EmailStr
    password:str
    phone_no:str
    role:str
    address:str
    hospital_id:int

class DoctorUpdate(BaseModel):
    phone_no:str
    address:str

class DoctorLogin(BaseModel):
    email:EmailStr
    password:str