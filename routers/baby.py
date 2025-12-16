from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.baby_model import Baby
from schemas.baby_schema import BabyCreate,BabyUpdate

router=APIRouter(
    prefix="/baby",
    tags=["Baby"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_baby(db:Session=Depends(get_db)):
    val=db.query(Baby).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Baby).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_baby(baby:BabyCreate,db:Session=Depends(get_db)):
    val=Baby(
        name=baby.name,
        phone_no=baby.phone_no,
        date_of_birth=baby.date_of_birth
    )
    db.add(val)
    db.commit()
    return val

@router.put("/update/{id}",status_code=status.HTTP_200_OK)
def update_detail(id:int,baby:BabyUpdate,db:Session=Depends(get_db)):
    val=db.query(Baby).filter(Baby.id==id).first()
    val.phone_no=baby.phone_no
    db.commit()
    return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_baby(id:int,db:Session=Depends(get_db)):
    val=db.query(Baby).filter(Baby.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}