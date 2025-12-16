from db.database import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Health_record(Base):
    __tablename__ = "health_record"

    id = Column(Integer, primary_key=True, autoincrement=True)
    baby_id = Column(Integer, ForeignKey("baby.id"), nullable=False)

    age_weeks = Column(Integer)
    bmi = Column(Float)
    notes = Column(String)

    baby = relationship("Baby", back_populates="health_records")


