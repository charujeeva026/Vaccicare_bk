import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import settings
from typing import List

def send_email(subject: str, recipients: List[str], body: str):

    msg = MIMEMultipart()
    msg["From"] = settings.MAIL_FROM
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP(settings.MAIL_SERVER, settings.MAIL_PORT)
        server.starttls()

        server.login(
            settings.MAIL_USERNAME,
            settings.MAIL_PASSWORD
        )

        server.send_message(msg)
        server.quit()

        print("Email sent successfully")

    except Exception as e:
        print("Email failed:", str(e))