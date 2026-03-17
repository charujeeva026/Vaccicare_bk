from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine
import models # Ensure all models are registered
from routers import (
    client,
    doctor,
    vaccine,
    hospital,
    vaccine_record,
    baby,
    reminder,
    health_record,
    appointment,
    contact,
    guideline
)
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from dependencies import get_db
from models.reminders_model import Reminders
from utils_email import send_email
from datetime import datetime, timedelta
import asyncio

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
    allow_origins=["*"],
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
# app.include_router(contact.router)
app.include_router(guideline.router)

# ---------------- ROOT ENDPOINT ----------------
@app.get("/")
def greet():
    return {"message": "Welcome to VacciCare API 🚀"}


# ================= EMAIL REMINDER JOB =================
def email_reminder_job():
    # Get a database session
    db: Session = next(get_db())
    today = datetime.now().date()

    # Fetch all reminders
    reminders = db.query(Reminders).all()

    for rem in reminders:
        baby = rem.baby
        client_email = baby.client.email
        vaccine_name = rem.vaccine_name
        vaccine_date = rem.date

        # 1 week before
        if vaccine_date - timedelta(days=7) == today:
            subject = "Vaccine Reminder: 1 Week Left"
            body = f"""
            <p>Hi {baby.name}'s parent,</p>
            <p>This is a reminder that <b>{vaccine_name}</b> is scheduled on {vaccine_date} (1 week left).</p>
            """
            asyncio.run(send_email(subject, [client_email], body))

        # 1 day before
        if vaccine_date - timedelta(days=1) == today:
            subject = "Vaccine Reminder: Tomorrow"
            body = f"""
            <p>Hi {baby.name}'s parent,</p>
            <p>This is a reminder that <b>{vaccine_name}</b> is scheduled tomorrow ({vaccine_date}).</p>
            """
            asyncio.run(send_email(subject, [client_email], body))


# ---------------- START SCHEDULER ----------------
scheduler = BackgroundScheduler()
scheduler.add_job(email_reminder_job, "interval", hours=24, next_run_time=datetime.now())
scheduler.start()


# ---------------- TEST EMAIL ----------------
@app.get("/test-email")
async def test_email():
    await send_email(
        subject="Test Email",
        recipients=["receiver@example.com"],
        body="<h1>Hello from VacciCare!</h1>"
    )
    return {"message": "Email sent!"}



