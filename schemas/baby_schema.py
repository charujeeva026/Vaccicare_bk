from pydantic import BaseModel

class BabyCreate(BaseModel):
    name:str
    date_of_birth:int
    phone_no:str
    gender:str

class BabyUpdate(BaseModel):
    phone_no:str
