from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # Encode as bytes and truncate to 72 bytes (bail-safe)
    password_bytes = password.encode("utf-8")[:72]
    # Ensure type is bytes (old passlib <=1.7.4 requires bytes)
    if isinstance(password_bytes, str):
        password_bytes = password_bytes.encode("utf-8")
    return pwd_context.hash(password_bytes)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = plain_password.encode("utf-8")[:72]
    if isinstance(password_bytes, str):
        password_bytes = password_bytes.encode("utf-8")
    return pwd_context.verify(password_bytes, hashed_password)