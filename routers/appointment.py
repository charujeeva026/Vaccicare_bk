from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.appointment_model import Appointment
from schemas.appointment_schema import AppointmentCreate

router = APIRouter(
    prefix="/appointment",
    tags=["Appointment"]
)

# GET ALL
@router.get("/home", status_code=status.HTTP_200_OK)
def get_all_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()


# GET BY ID
@router.get("/home/{id}", status_code=status.HTTP_200_OK)
def get_appointment(id: int, db: Session = Depends(get_db)):

    appointment = db.query(Appointment).filter(Appointment.id == id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment


# CREATE
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_appointment(booking: AppointmentCreate, db: Session = Depends(get_db)):

    new_appointment = Appointment(
        client_id=booking.client_id,
        doctor_id=booking.doctor_id,
        appointment_date=booking.appointment_date,
        appointment_time=booking.appointment_time
    )

    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return new_appointment


# DELETE
@router.delete("/delete/{id}")
def delete_appointment(id: int, db: Session = Depends(get_db)):

    appointment = db.query(Appointment).filter(Appointment.id == id).first()

    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(appointment)
    db.commit()

    return {"message": "Appointment deleted"}