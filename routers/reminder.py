from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.reminders_model import Reminders
from schemas.reminder_schema import ReminderCreate

router=APIRouter(
    prefix="/reminder",
    tags=["Reminder"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_reminder(db:Session=Depends(get_db)):
    val=db.query(Reminders).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Reminders).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_reminder(rem:ReminderCreate,db:Session=Depends(get_db)):
    val=Reminders(
        date=rem.date,
        day=rem.day,
        vaccine_name=rem.vaccine_name
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
def delete_reminder(id:int,db:Session=Depends(get_db)):
    val=db.query(Reminders).filter(Reminders.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}