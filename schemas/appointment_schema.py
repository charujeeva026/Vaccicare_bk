from pydantic import BaseModel,EmailStr
from datetime import date, time


class AppointmentCreate(BaseModel):
    client_id:int
    baby_id:int
    doctor_id:int
    date: date
    time: time

    
   