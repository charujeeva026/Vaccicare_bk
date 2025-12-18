from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.doctor_model import Doctor
from schemas.doctor_schema import DoctorCreate,DoctorUpdate

router=APIRouter(
    prefix="/doctor",
    tags=["Doctor"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_user(db:Session=Depends(get_db)):
    val=db.query(Doctor).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Doctor).get(id)
    return val

@router.post("/create",status_code=status.HTTP_200_OK)
def create_doctor(doctor:DoctorCreate,db:Session=Depends(get_db)):
    val=Doctor(
        name=doctor.name,
        email=doctor.email,
        password=doctor.password,
        phone_no=doctor.phone_no,
        role=doctor.role,
        address=doctor.address
    )
    db.add(val)
    db.commit()
    return val

@router.put("/update/{id}",status_code=status.HTTP_200_OK)
def update_detail(id:int,doctor:DoctorUpdate,db:Session=Depends(get_db)):
    val=db.query(Doctor).filter(Doctor.id==id).first()
    val.phone_no=doctor.phone_no,
    val.address=doctor.address
    db.commit()
    return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_doctor(id:int,db:Session=Depends(get_db)):
    val=db.query(Doctor).filter(Doctor.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}