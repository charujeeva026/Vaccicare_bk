from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from dependencies import get_db
from models.vaccine_model import Vaccine
from schemas.vaccine_schema import VaccineCreate, VaccineUpdate, VaccineSchema

router = APIRouter(
    prefix="/vaccine",
    tags=["Vaccine"]
)

# ================= GET ALL VACCINES =================
@router.get("/home", response_model=List[VaccineSchema], status_code=status.HTTP_200_OK)
def get_all_vaccine(db: Session = Depends(get_db)):
    return db.query(Vaccine).all()

# ================= GET VACCINE BY ID =================
@router.get("/home/{id}", response_model=VaccineSchema, status_code=status.HTTP_200_OK)
def get_id(id: int, db: Session = Depends(get_db)):
    val = db.query(Vaccine).get(id)
    return val

# ================= CREATE VACCINE =================
@router.post("/create", response_model=VaccineSchema, status_code=status.HTTP_200_OK)
def create_vaccine(vaccine: VaccineCreate, db: Session = Depends(get_db)):
    val = Vaccine(
        vaccine_name=vaccine.vaccine_name,
        age_weeks=vaccine.age_weeks
    )
    db.add(val)
    db.commit()
    db.refresh(val)  # <- ensure returned object has id
    return val

# ================= UPDATE VACCINE =================
@router.put("/update/{id}", response_model=VaccineSchema, status_code=status.HTTP_200_OK)
def update_detail(id: int, vaccine: VaccineUpdate, db: Session = Depends(get_db)):
    val = db.query(Vaccine).filter(Vaccine.id == id).first()
    val.age_weeks = vaccine.age_weeks
    db.commit()
    db.refresh(val)
    return val

# ================= DELETE VACCINE =================
@router.delete("/delete_user/{id}", status_code=status.HTTP_200_OK)
def delete_vaccine(id: int, db: Session = Depends(get_db)):
    val = db.query(Vaccine).filter(Vaccine.id == id).first()
    db.delete(val)
    db.commit()
    return {"msg": "Successfully deleted"}