from pydantic import BaseModel
from datetime import date

class ReminderCreate(BaseModel):
    baby_id:int
    date:date
    day:str
    vaccine_name:str

