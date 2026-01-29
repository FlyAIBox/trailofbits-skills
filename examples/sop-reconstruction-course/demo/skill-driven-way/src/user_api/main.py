"""FastAPI application for user registration."""

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import models, schemas
from .auth import create_access_token, hash_password
from .database import get_db, init_db

app = FastAPI(
    title="User Registration API",
    description="Secure user registration with JWT authentication",
    version="0.1.0",
)


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database on application startup."""
    init_db()


@app.post(
    "/register",
    response_model=schemas.UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    responses={
        201: {"description": "User successfully registered"},
        400: {"description": "Username or email already exists"},
        422: {"description": "Validation error"},
    },
)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)) -> dict:
    """
    Register a new user.

    This endpoint:
    1. Validates input (username, email format, password strength)
    2. Checks for duplicate username/email (via DB constraint)
    3. Hashes password with bcrypt (12 rounds)
    4. Stores user in database
    5. Returns user_id and JWT token

    Args:
        user: User registration data
        db: Database session (injected)

    Returns:
        UserResponse with user_id and JWT token

    Raises:
        HTTPException: 400 if username/email already exists
    """
    # Hash password (bcrypt with configured rounds)
    hashed_password = hash_password(user.password)

    # Create user object
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )

    try:
        # Save to database
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

    except IntegrityError:
        # This catches duplicate username/email (UNIQUE constraint violation)
        # Also handles race conditions where two requests try to create same user
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists",
        ) from None

    # Generate JWT token
    token = create_access_token({"sub": str(db_user.id)})

    return {
        "user_id": db_user.id,
        "token": token,
    }


@app.get("/health")
def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}

