from db.database import Base
from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    phone_no = Column(String)
    role = Column(String)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    hospital_id = Column(Integer, ForeignKey("hospital.id"))

    hospital = relationship("Hospital", back_populates="doctors")
    appointments = relationship("Appointment", back_populates="doctor")