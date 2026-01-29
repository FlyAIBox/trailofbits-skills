"""JWT token generation and password hashing utilities."""

from datetime import datetime, timedelta, timezone

import bcrypt
import jwt

from .config import settings


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.

    Args:
        password: Plain text password

    Returns:
        Hashed password as bytes

    Example:
        >>> hashed = hash_password("SecureP@ssw0rd")
        >>> isinstance(hashed, bytes)
        True
    """
    salt = bcrypt.gensalt(rounds=settings.bcrypt_rounds)
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def verify_password(password: str, hashed_password: bytes) -> bool:
    """
    Verify a password against its hash.

    Args:
        password: Plain text password
        hashed_password: Hashed password from database

    Returns:
        True if password matches, False otherwise
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create a JWT access token.

    Args:
        data: Payload data to encode
        expires_delta: Token expiration time (default: from settings)

    Returns:
        Encoded JWT token

    Example:
        >>> token = create_access_token({"sub": "123"})
        >>> isinstance(token, str)
        True
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )

    to_encode.update({"exp": expire, "iat": datetime.now(timezone.utc)})

    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def decode_access_token(token: str) -> dict:
    """
    Decode and verify a JWT access token.

    Args:
        token: JWT token to decode

    Returns:
        Decoded payload

    Raises:
        jwt.InvalidTokenError: If token is invalid or expired
    """
    return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])

