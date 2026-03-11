from pydantic import BaseModel
from datetime import date, time

class AppointmentCreate(BaseModel):

    client_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time

    class Config:
        from_attributes = True