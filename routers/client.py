from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from utils_security import hash_password, verify_password

from models.client_model import Client
from schemas.client_schema import (
    ClientCreate,
    ClientUpdate,
    ClientLogin,
    ClientResponse,
)

router = APIRouter(prefix="/client", tags=["Client"])


# ---------------- GET ALL CLIENTS ----------------
@router.get("/", response_model=list[ClientResponse])
def get_all_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()


# ---------------- GET CLIENT PROFILE ----------------
@router.get("/profile/{id}", response_model=ClientResponse)
def get_client_profile(id: int, db: Session = Depends(get_db)):

    client = db.query(Client).filter(Client.id == id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    return client


# ---------------- CREATE CLIENT ----------------
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):

    existing_client = db.query(Client).filter(Client.email == client.email).first()

    if existing_client:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(client.password)

    new_client = Client(
        name=client.name,
        email=client.email,
        password=hashed_password,
        phone_no=client.phone_no,
        address=client.address,
        location=client.location,
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return {"message": "Client created successfully", "client_id": new_client.id}


# ---------------- LOGIN CLIENT ----------------
@router.post("/login")
def login_client(data: ClientLogin, db: Session = Depends(get_db)):

    client = db.query(Client).filter(Client.email == data.email).first()

    if not client:
        raise HTTPException(status_code=404, detail="Email not registered")

    if not verify_password(data.password, client.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "client_id": client.id,
        "name": client.name,
        "role": "Client",
    }


# ---------------- UPDATE PROFILE ----------------
@router.put("/update/{id}", response_model=ClientResponse)
def update_client(id: int, client: ClientUpdate, db: Session = Depends(get_db)):

    existing_client = db.query(Client).filter(Client.id == id).first()

    if not existing_client:
        raise HTTPException(status_code=404, detail="Client not found")

    if client.phone_no is not None:
        existing_client.phone_no = client.phone_no

    if client.address is not None:
        existing_client.address = client.address

    if client.location is not None:
        existing_client.location = client.location

    db.commit()
    db.refresh(existing_client)

    return existing_client


# ---------------- DELETE CLIENT ----------------
@router.delete("/delete/{id}")
def delete_client(id: int, db: Session = Depends(get_db)):

    client = db.query(Client).filter(Client.id == id).first()

    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    db.delete(client)
    db.commit()

    return {"message": "Client deleted successfully"}