from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.reminders_model import Reminders
from models.client_model import Client
from schemas.reminder_schema import ReminderCreate, ReminderSchema
from typing import List

router = APIRouter(prefix="/reminder", tags=["Reminder"])

# ---------------- GET ALL REMINDERS ----------------
@router.get("/home", response_model=List[ReminderSchema], status_code=status.HTTP_200_OK)
def get_all_reminder(db: Session = Depends(get_db)):
    return db.query(Reminders).all()

# ---------------- GET REMINDER BY ID ----------------
@router.get("/home/{id}", response_model=ReminderSchema, status_code=status.HTTP_200_OK)
def get_id(id: int, db: Session = Depends(get_db)):
    val = db.query(Reminders).get(id)
    if not val:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return val

# ---------------- CREATE REMINDER ----------------
@router.post("/create", response_model=ReminderSchema, status_code=status.HTTP_201_CREATED)
def create_reminder(rem: ReminderCreate, db: Session = Depends(get_db)):
    # check if client exists
    client = db.query(Client).filter(Client.id == rem.client_id).first()
    if not client:
        raise HTTPException(status_code=400, detail="Invalid client_id")

    val = Reminders(
        client_id=rem.client_id,
        vaccine_name=rem.vaccine_name,
        date=rem.date,
        day=rem.day
    )
    db.add(val)
    db.commit()
    db.refresh(val)
    return val

# ---------------- DELETE REMINDER ----------------
@router.delete("/delete_user/{id}", status_code=status.HTTP_200_OK)
def delete_reminder(id: int, db: Session = Depends(get_db)):
    val = db.query(Reminders).filter(Reminders.id == id).first()
    if not val:
        raise HTTPException(status_code=404, detail="Reminder not found")
    db.delete(val)
    db.commit()
    return {"msg": "Successfully deleted"}