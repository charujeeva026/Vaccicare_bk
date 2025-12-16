from pydantic import BaseModel
from datetime import date

class Vaccine_recordsCreate(BaseModel):
    date_given:date
    next_date:date
    status:str

class Vaccine_recordsUpdate(BaseModel):
    next_date:date
    status:str