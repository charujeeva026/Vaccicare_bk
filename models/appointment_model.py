from db.database import Base
from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

class Appointment(Base):
    __tablename__ = "appointment"

    id = Column(Integer, primary_key=True, autoincrement=True)

    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    baby_id = Column(Integer, ForeignKey("baby.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctor.id"), nullable=False)

    date = Column(Date)
    time = Column(Time)

    client = relationship("Client", back_populates="appointments")
    baby = relationship("Baby", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")






