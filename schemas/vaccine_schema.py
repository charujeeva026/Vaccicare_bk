from pydantic import BaseModel

# For creating vaccine
class VaccineCreate(BaseModel):
    vaccine_name: str
    age_weeks: str

# For updating vaccine
class VaccineUpdate(BaseModel):
    age_weeks: str

# For GET response (dropdown)
class VaccineSchema(BaseModel):
    id: int
    vaccine_name: str

    class Config:
        orm_mode = True