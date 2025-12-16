from fastapi import FastAPI
from db.database import Base,engine
from routers import client,doctor,vaccine,hospital,vaccine_record,baby,reminder,health_record,appointment

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(client.router)
app.include_router(doctor.router)
app.include_router(vaccine.router)
app.include_router(hospital.router)
app.include_router(vaccine_record.router)
app.include_router(baby.router)
app.include_router(reminder.router)
app.include_router(health_record.router)
app.include_router(appointment.router)

@app.get("/")
def greet():
    return "welcome"