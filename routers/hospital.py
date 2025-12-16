from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.hospital_model import Hospital
from schemas.hospital_schema import HospitalCreate,HospitalUpdate

router=APIRouter(
    prefix="/hospital",
    tags=["Hospital"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_hospital(db:Session=Depends(get_db)):
    val=db.query(Hospital).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Hospital).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_hospital(hospital:HospitalCreate,db:Session=Depends(get_db)):
    val=Hospital(
        hospital_name=hospital.hospital_name,
        contact_number=hospital.contact_number,
        address=hospital.address,
        distance=hospital.distance
    )
    db.add(val)
    db.commit()
    return val

@router.put("/update/{id}",status_code=status.HTTP_200_OK)
def update_detail(id:int,hospital:HospitalUpdate,db:Session=Depends(get_db)):
    val=db.query(Hospital).filter(Hospital.id==id).first()
    val.contact_number=hospital.contact_number,
    val.address=hospital.address
    db.commit()
    return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_hospital(id:int,db:Session=Depends(get_db)):
    val=db.query(Hospital).filter(Hospital.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}