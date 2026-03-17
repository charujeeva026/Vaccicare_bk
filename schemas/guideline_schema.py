from pydantic import BaseModel

class GuidelineCreate(BaseModel):
    month: int
    healthy_eating: str
    exercise_meditation: str
    daily_habits: str
    mental_wellbeing: str

class GuidelineResponse(GuidelineCreate):
    id: int

    class Config:
        from_attributes = True
