from pydantic import BaseModel,EmailStr

class Health_recordCreate(BaseModel):
    baby_id:int
    age_weeks:int
    notes:str
    bmi:float

