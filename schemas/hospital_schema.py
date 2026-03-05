from pydantic import BaseModel,EmailStr

class HospitalCreate(BaseModel):
    hospital_name:str
    address:str
    contact_number:str
    distance:int

class HospitalUpdate(BaseModel):
    contact_number:str
    address:str