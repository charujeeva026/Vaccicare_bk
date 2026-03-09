from db.database import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Reminders(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)  # changed from baby_id
    vaccine_name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    day = Column(String, nullable=False)

    # Relationship with Client table
    client = relationship("Client", back_populates="reminders")