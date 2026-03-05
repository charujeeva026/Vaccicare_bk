from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db.database import Base, engine
from routers import (
    client,
    doctor,
    vaccine,
    hospital,
    vaccine_record,
    baby,
    reminder,
    health_record,
    appointment
)

# ---------------- CREATE TABLES ----------------
Base.metadata.create_all(bind=engine)

# ---------------- APP INSTANCE ----------------
app = FastAPI(
    title="VacciCare API",
    version="1.0.0"
)

# ---------------- CORS MIDDLEWARE ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠ For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- ROUTERS ----------------
app.include_router(client.router)
app.include_router(doctor.router)
app.include_router(vaccine.router)
app.include_router(hospital.router)
app.include_router(vaccine_record.router)
app.include_router(baby.router)
app.include_router(reminder.router)
app.include_router(health_record.router)
app.include_router(appointment.router)

# ---------------- ROOT ENDPOINT ----------------
@app.get("/")
def greet():
    return {"message": "Welcome to VacciCare API 🚀"}
