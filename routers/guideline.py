from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_db
from models.guideline_model import Guideline
from schemas.guideline_schema import GuidelineCreate, GuidelineResponse

router = APIRouter(
    prefix="/guidelines",
    tags=["Guidelines"]
)

@router.get("/{month}", response_model=GuidelineResponse)
def get_guideline_by_month(month: int, db: Session = Depends(get_db)):
    guideline = db.query(Guideline).filter(Guideline.month == month).first()
    if not guideline:
        raise HTTPException(status_code=404, detail="Guideline not found for this month")
    return guideline

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_guideline(data: GuidelineCreate, db: Session = Depends(get_db)):
    existing = db.query(Guideline).filter(Guideline.month == data.month).first()
    if existing:
        raise HTTPException(status_code=400, detail="Guideline for this month already exists")

    new_guideline = Guideline(
        month=data.month,
        healthy_eating=data.healthy_eating,
        exercise_meditation=data.exercise_meditation,
        daily_habits=data.daily_habits,
        mental_wellbeing=data.mental_wellbeing
    )

    db.add(new_guideline)
    db.commit()
    db.refresh(new_guideline)

    return {"message": "Guideline created successfully"}
