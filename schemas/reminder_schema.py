from pydantic import BaseModel
from datetime import date

class ReminderCreate(BaseModel):
    date:date
    day:str
    vaccine_name:str

