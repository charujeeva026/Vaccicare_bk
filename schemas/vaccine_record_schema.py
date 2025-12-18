from pydantic import BaseModel
from datetime import date

class Vaccine_recordsCreate(BaseModel):
    baby_id:int
    vaccine_id:int
    date_given:date
    next_date:date
    status:str

class Vaccine_recordsUpdate(BaseModel):
    next_date:date
    status:str