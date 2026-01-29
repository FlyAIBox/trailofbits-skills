"""Pydantic schemas for request/response validation."""

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    """Schema for user registration request."""

    username: str = Field(..., min_length=3, max_length=50, pattern="^[a-zA-Z0-9_-]+$")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        """
        Validate password strength.

        Password must contain:
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character
        """
        if not any(c.isupper() for c in v):
            msg = "Password must contain at least one uppercase letter"
            raise ValueError(msg)
        if not any(c.islower() for c in v):
            msg = "Password must contain at least one lowercase letter"
            raise ValueError(msg)
        if not any(c.isdigit() for c in v):
            msg = "Password must contain at least one digit"
            raise ValueError(msg)
        if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in v):
            msg = "Password must contain at least one special character"
            raise ValueError(msg)
        return v


class UserResponse(BaseModel):
    """Schema for user registration response."""

    user_id: int
    token: str

    model_config = {"from_attributes": True}

