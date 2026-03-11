from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    # Convert password to SHA256 first (fixed length)
    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    # Truncate to 72 bytes for bcrypt safety
    sha256_hash = sha256_hash[:72]
    return pwd_context.hash(sha256_hash)

def verify_password(plain_password: str, hashed_password: str):
    sha256_hash = hashlib.sha256(plain_password.encode()).hexdigest()
    sha256_hash = sha256_hash[:72]
    return pwd_context.verify(sha256_hash, hashed_password)