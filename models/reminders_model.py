from db.database import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Reminders(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    baby_id = Column(Integer, ForeignKey("baby.id"), nullable=False)

    date = Column(Date)
    day = Column(String)
    vaccine_name = Column(String)

    baby = relationship("Baby")


