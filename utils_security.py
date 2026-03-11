from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash password safely:
    1. Encode as bytes
    2. SHA256 digest → 32 bytes
    3. bcrypt hash
    """
    password_bytes = password.encode("utf-8")            # Encode
    sha256_bytes = hashlib.sha256(password_bytes).digest()  # 32 bytes
    return pwd_context.hash(sha256_bytes)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha256_bytes = hashlib.sha256(plain_password.encode("utf-8")).digest()
    return pwd_context.verify(sha256_bytes, hashed_password)