from db.database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Client(Base):
    __tablename__ = "client"  # keep as "client"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    phone_no = Column(String)
    address = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    babies = relationship("Baby", back_populates="client")
    appointments = relationship("Appointment", back_populates="client")
    reminders = relationship("Reminders", back_populates="client")  # added for reminders