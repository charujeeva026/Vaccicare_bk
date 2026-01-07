from db.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class Hospital(Base):
    __tablename__ = "hospital"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hospital_name = Column(String)
    address = Column(String)
    contact_number = Column(String)
    distance = Column(String)

    doctors = relationship("Doctor", back_populates="hospital")



