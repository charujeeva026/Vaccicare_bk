from db.database import Base
from sqlalchemy import Column, Integer, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

class Appointment(Base):
    __tablename__ = "appointment"

    id = Column(Integer, primary_key=True, autoincrement=True)

    client_id = Column(Integer, ForeignKey("client.id"))
    doctor_id = Column(Integer, ForeignKey("doctor.id"))

    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)

    client = relationship("Client", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")