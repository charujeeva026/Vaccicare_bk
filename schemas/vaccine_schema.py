from pydantic import BaseModel

class VaccineCreate(BaseModel):
    vaccine_name:str
    age_weeks:int
  

class VaccineUpdate(BaseModel):
    age_weeks:int