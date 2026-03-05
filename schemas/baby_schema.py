from pydantic import BaseModel,EmailStr

class BabyCreate(BaseModel):
    client_id:int
    name:str
    date_of_birth:str
    phone_no:str
    gender:str

class BabyUpdate(BaseModel):
    phone_no:str
