from pydantic import BaseModel
from datetime import date

class ReminderCreate(BaseModel):
    client_id: int
    vaccine_name: str
    date: date
    day: str

class ReminderSchema(BaseModel):
    id: int
    client_id: int
    vaccine_name: str
    date: date
    day: str

    class Config:
        from_attributes = True