from db.database import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Baby(Base):
    __tablename__ = "baby"

    id = Column(Integer, primary_key=True, autoincrement=True)

    client_id = Column(Integer, ForeignKey("client.id"))

    name = Column(String)
    date_of_birth = Column(Date)
    phone_no = Column(String)
    gender = Column(String)

    client = relationship("Client", back_populates="babies")
    health_records = relationship("HealthRecord", back_populates="baby")
    vaccine_records = relationship("VaccineRecords", back_populates="baby")