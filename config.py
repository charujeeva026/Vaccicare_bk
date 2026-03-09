from pydantic_settings import BaseSettings
from pydantic import EmailStr

class Settings(BaseSettings):

    MAIL_USERNAME: str = "yourgmail@gmail.com"
    MAIL_PASSWORD: str = "your_google_app_password"
    MAIL_FROM: EmailStr = "yourgmail@gmail.com"

    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"

    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False

    class Config:
        extra = "ignore"


settings = Settings()