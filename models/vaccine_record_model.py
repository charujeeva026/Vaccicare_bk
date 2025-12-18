from db.database import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class VaccineRecords(Base):
    __tablename__ = "vaccine_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    baby_id = Column(Integer, ForeignKey("baby.id") )
    vaccine_id = Column(Integer, ForeignKey("vaccine.id"))

    date_given = Column(Date)
    next_date = Column(Date)
    status = Column(String)

    baby = relationship("Baby", back_populates="vaccine_records")
    vaccine = relationship("Vaccine", back_populates="records")



