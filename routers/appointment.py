from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.appointment_model import Appointment
from schemas.appointment_schema import AppointmentCreate

router=APIRouter(
    prefix="/appointment",
    tags=["Appointment"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_appointment(db:Session=Depends(get_db)):
    val=db.query(Appointment).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Appointment).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_appointment(booking:AppointmentCreate,db:Session=Depends(get_db)):
    val=Appointment(
        date=booking.date,
        time=booking.time
    )
    db.add(val)
    db.commit()
    return val

# @router.put("/update/{id}")
# def update_detail(id:int,baby:BabyUpdate,db:Session=Depends(get_db)):
#     val=db.query(Baby).filter(Baby.id==id).first()
#     val.phone_no=baby.phone_no
#     db.commit()
#     return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_appointment(id:int,db:Session=Depends(get_db)):
    val=db.query(Appointment).filter(Appointment.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}