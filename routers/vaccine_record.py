from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.vaccine_record_model import Vaccine_records
from schemas.vaccine_record_schema import Vaccine_recordsCreate,Vaccine_recordsUpdate

router=APIRouter(
    prefix="/vaccine_records",
    tags=["Vaccine_records"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_vaccine_record(db:Session=Depends(get_db)):
    val=db.query(Vaccine_records).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Vaccine_records).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_vaccine_records(record:Vaccine_recordsCreate,db:Session=Depends(get_db)):
    val=Vaccine_records(
       date_given=record.date_given,
       next_date=record.next_date,
       status=record.status
    )
    db.add(val)
    db.commit()
    return val

@router.put("/update/{id}",status_code=status.HTTP_200_OK)
def update_detail(id:int,record:Vaccine_recordsUpdate,db:Session=Depends(get_db)):
    val=db.query(Vaccine_records).filter(Vaccine_records.id==id).first()
    val.next_date=record.next_date,
    val.status=record.status
    db.commit()
    return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_vaccine_record(id:int,db:Session=Depends(get_db)):
    val=db.query(Vaccine_records).filter(Vaccine_records.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}