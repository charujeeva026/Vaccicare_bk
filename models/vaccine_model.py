from db.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Vaccine(Base):
    __tablename__ = "vaccine"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vaccine_name = Column(String)
    age_weeks = Column(Integer)

    records = relationship("VaccineRecord", back_populates="vaccine")



