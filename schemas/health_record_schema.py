from pydantic import BaseModel

class Health_recordCreate(BaseModel):
    baby_id:int
    age_weeks:int
    notes:str
    bmi:float

