from pydantic import BaseModel

class Health_recordCreate(BaseModel):
    age_weeks:int
    notes:str
    bmi:float

