from pydantic import BaseModel
from datetime import date, time

class AppointmentCreate(BaseModel):
    date: date
    time: time

    
   