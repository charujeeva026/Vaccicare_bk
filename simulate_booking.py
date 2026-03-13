import os
import sys
from datetime import date, time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Add current dir to sys.path to import models
sys.path.append(os.getcwd())

from db.database import Base, SessionLocal
import models # This triggers the imports in models/__init__.py
from models.appointment_model import Appointment

def simulate_create():
    db = SessionLocal()
    try:
        # Client ID 16 exists, Doctor ID 5 exists in Neon
        # Let's try to create one
        new_appointment = Appointment(
            client_id=16,
            doctor_id=5,
            appointment_date=date(2026, 3, 20),
            appointment_time=time(10, 0, 0)
        )
        
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        print(f"Successfully created appointment ID: {new_appointment.id}")
        
    except Exception as e:
        print(f"Error creating appointment: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    simulate_create()
