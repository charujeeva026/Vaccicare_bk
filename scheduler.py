from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from db.database import get_db
from models.reminders_model import Reminders
from utils_email import send_email
import asyncio

def check_reminders():
    db: Session = next(get_db())  # get DB session

    today = datetime.now().date()

    reminders = db.query(Reminders).all()

    for rem in reminders:
        # Convert date to datetime.date if not already
        rem_date = rem.date

        # One week before
        if rem_date - timedelta(days=7) == today:
            asyncio.run(send_email(
                subject=f"Vaccine Reminder: {rem.vaccine_name}",
                recipients=[rem.baby.client.email],  # assuming relationship is set
                body=f"Reminder: {rem.vaccine_name} vaccine is due in 1 week on {rem_date}"
            ))

        # One day before
        if rem_date - timedelta(days=1) == today:
            asyncio.run(send_email(
                subject=f"Vaccine Reminder: {rem.vaccine_name}",
                recipients=[rem.baby.client.email],
                body=f"Reminder: {rem.vaccine_name} vaccine is tomorrow ({rem_date})"
            ))

scheduler = BackgroundScheduler()
scheduler.add_job(check_reminders, "interval", hours=24)  # check every day
scheduler.start()