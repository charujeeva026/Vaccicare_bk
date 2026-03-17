from db.database import Base
from sqlalchemy import Column, Integer, Text

class Guideline(Base):
    __tablename__ = "guidelines"

    id = Column(Integer, primary_key=True, autoincrement=True)
    month = Column(Integer, unique=True, index=True)

    healthy_eating = Column(Text)
    exercise_meditation = Column(Text)
    daily_habits = Column(Text)
    mental_wellbeing = Column(Text)
