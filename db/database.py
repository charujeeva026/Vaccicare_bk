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
    
    # Ensure it uses psycopg2 driver explicitly
    if DATABASE_URL.startswith("postgresql://") and "+psycopg2" not in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)
        
    print(f"DATABASE_URL found. Connecting to database...")
    engine = create_engine(DATABASE_URL)
else:
    print("Warning: DATABASE_URL not found. Database features will not work.")
    engine = create_engine("sqlite:///:memory:") 

try:
    # Test the connection immediately
    with engine.connect() as connection:
        print("Successfully connected to the database!")
except Exception as e:
    print(f"Database connection error: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()