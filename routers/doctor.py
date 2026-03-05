from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from dependencies import get_db
from models.doctor_model import Doctor
from schemas.doctor_schema import DoctorCreate, DoctorUpdate, DoctorLogin
from utils_security import hash_password, verify_password

router = APIRouter(
    prefix="/doctor",
    tags=["Doctor"]
)

# ---------------- GET ALL DOCTORS ----------------
@router.get("/home", status_code=status.HTTP_200_OK)
def get_all_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()


# ---------------- GET DOCTOR BY ID ----------------
@router.get("/home/{id}", status_code=status.HTTP_200_OK)
def get_doctor_by_id(id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


# ---------------- CREATE DOCTOR ----------------
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):

    existing = db.query(Doctor).filter(
        func.lower(Doctor.email) == doctor.email.lower()
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_doctor = Doctor(
        name=doctor.name,
        email=doctor.email.lower(),
        password=hash_password(doctor.password),  # ✅ HASHED
        phone_no=doctor.phone_no,
        role=doctor.role,
        address=doctor.address,
        hospital_id=doctor.hospital_id
    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return {
        "message": "Doctor account created successfully",
        "doctor_id": new_doctor.id
    }


# ---------------- DOCTOR LOGIN 🔥 ----------------
@router.post("/login")
def doctor_login(request: DoctorLogin, db: Session = Depends(get_db)):

    doctor = db.query(Doctor).filter(
        Doctor.email == request.email
    ).first()

    if not doctor:
        raise HTTPException(status_code=400, detail="Doctor not found")

    if not verify_password(request.password, doctor.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    return {
        "message": "Login successful",
        "doctor_id": doctor.id,
        "role": "Doctor"
    }

# ---------------- UPDATE DOCTOR ----------------
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def update_doctor(id: int, doctor: DoctorUpdate, db: Session = Depends(get_db)):

    existing_doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if not existing_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    if doctor.phone_no:
        existing_doctor.phone_no = doctor.phone_no
    if doctor.address:
        existing_doctor.address = doctor.address

    db.commit()
    db.refresh(existing_doctor)

    return {"message": "Doctor updated successfully"}


# ---------------- DELETE DOCTOR ----------------
@router.delete("/delete_user/{id}", status_code=status.HTTP_200_OK)
def delete_doctor(id: int, db: Session = Depends(get_db)):

    doctor = db.query(Doctor).filter(Doctor.id == id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(doctor)
    db.commit()

    return {"message": "Doctor deleted successfully"}