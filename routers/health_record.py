from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.health_records_model import HealthRecord
from schemas.health_record_schema import Health_recordCreate

router=APIRouter(
    prefix="/health_record",
    tags=["Health_record"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_health_records(db:Session=Depends(get_db)):
    val=db.query(HealthRecord).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(HealthRecord).get(id)
    return val

@router.post("/create",status_code=status.HTTP_200_OK)
def create_health_record(record:Health_recordCreate,db:Session=Depends(get_db)):
    val=HealthRecord(
        baby_id=record.baby_id,
       age_weeks=record.age_weeks,
       notes=record.notes,
       bmi=record.bmi
    )
    db.add(val)
    db.commit()
    db.refresh(val)
    return val

# @router.put("/update/{id}")
# def update_detail(id:int,baby:BabyUpdate,db:Session=Depends(get_db)):
#     val=db.query(Baby).filter(Baby.id==id).first()
#     val.phone_no=baby.phone_no
#     db.commit()
#     return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_health_record(id:int,db:Session=Depends(get_db)):
    val=db.query(HealthRecord).filter(HealthRecord.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}