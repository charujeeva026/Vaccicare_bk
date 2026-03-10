from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("database_url") or os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print("Warning: DATABASE_URL not found in environment variables.")
else:
    print("DATABASE_URL found.")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()