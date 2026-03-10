from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("database_url") or os.getenv("DATABASE_URL")

if DATABASE_URL:
    # SQLAlchemy 1.4+ and 2.0+ require 'postgresql://' instead of 'postgres://'
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    print("DATABASE_URL found and configured.")
    engine = create_engine(DATABASE_URL)
else:
    print("Warning: DATABASE_URL not found. Database features will not work.")
    # Create a dummy engine to prevent import errors, though queries will fail
    engine = create_engine("sqlite:///:memory:") 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()