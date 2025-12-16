from db.database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    phone_no = Column(String)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    babies = relationship("Baby", back_populates="client")
    appointments = relationship("Appointment", back_populates="client")



