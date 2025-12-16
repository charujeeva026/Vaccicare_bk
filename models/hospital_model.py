from db.database import Base
from sqlalchemy import Column, String, Integer

class Hospital(Base):
    __tablename__ = "hospital"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hospital_name = Column(String)
    address = Column(String)
    contact_number = Column(String)
    distance = Column(String)



