from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    # Encode password as bytes
    password_bytes = password.encode('utf-8')
    # Truncate to 72 bytes to avoid bcrypt errors
    password_bytes = password_bytes[:72]
    # Hash using bcrypt directly
    return pwd_context.hash(password_bytes)

def verify_password(plain_password: str, hashed_password: str):
    password_bytes = plain_password.encode('utf-8')[:72]
    return pwd_context.verify(password_bytes, hashed_password)