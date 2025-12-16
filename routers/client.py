from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from dependencies import get_db
from models.client_model import Client
from schemas.client_schema import ClientCreate,ClientUpdate

router=APIRouter(
    prefix="/client",
    tags=["Client"]
)

@router.get("/home",status_code=status.HTTP_200_OK)
def get_all_user(db:Session=Depends(get_db)):
    val=db.query(Client).all()
    return val

@router.get('/home/{id}',status_code=status.HTTP_200_OK)
def get_id(id:int,db:Session=Depends(get_db)):
    val=db.query(Client).get(id)

@router.post("/create",status_code=status.HTTP_200_OK)
def create_client(client:ClientCreate,db:Session=Depends(get_db)):
    val=Client(
        name=client.name,
        email=client.email,
        password=client.password,
        phone_no=client.phone_no,
        address=client.address
    )
    db.add(val)
    db.commit()
    return val

@router.put("/update/{id}",status_code=status.HTTP_200_OK)
def update_detail(id:int,client:ClientUpdate,db:Session=Depends(get_db)):
    val=db.query(Client).filter(Client.id==id).first()
    val.phone_no=client.phone_no,
    val.address=client.address
    db.commit()
    return val

@router.delete("/delete_user/{id}",status_code=status.HTTP_200_OK)
def delete_client(id:int,db:Session=Depends(get_db)):
    val=db.query(Client).filter(Client.id==id).first()
    db.delete(val)
    db.commit()
    return {"msg":"Successfully deleted"}