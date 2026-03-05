from pydantic import BaseModel, EmailStr
from typing import Optional


# ---------- CREATE ----------
class ClientCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone_no: str
    address: str
    location: str


# ---------- LOGIN ----------
class ClientLogin(BaseModel):
    email: EmailStr
    password: str


# ---------- UPDATE ----------
class ClientUpdate(BaseModel):
    phone_no: Optional[str] = None
    address: Optional[str] = None
    location: Optional[str] = None


# ---------- RESPONSE ----------
class ClientResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone_no: str
    address: str
    location: str

    class Config:
        from_attributes = True
