from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.vaccine_model import Vaccine
from schemas.vaccine_schema import VaccineCreate,VaccineUpdate

router=APIRouter(
    prefix="/vaccine",
    tags=["Vaccine"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_vaccine(db:Session=Depends(get_db)):
    val=db.query(Vaccine).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Vaccine).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_vaccine(vaccine:VaccineCreate,db:Session=Depends(get_db)):
    val=Vaccine(
        vaccine_name=vaccine.vaccine_name,
        age_weeks=vaccine.age_weeks
    )
    db.add(val)
    db.commit()
    return val

@router.put("/update/{id}",status_code=status.HTTP_200_OK)
def update_detail(id:int,vaccine:VaccineUpdate,db:Session=Depends(get_db)):
    val=db.query(Vaccine).filter(Vaccine.id==id).first()
    val.age_weeks=vaccine.age_weeks
    db.commit()
    return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_vaccine(id:int,db:Session=Depends(get_db)):
    val=db.query(Vaccine).filter(Vaccine.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}