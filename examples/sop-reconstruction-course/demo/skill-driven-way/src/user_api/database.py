"""Database connection and session management."""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from .config import settings

# Create engine
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,  # Verify connections before using
    echo=False,
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency that provides a database session.

    Yields:
        Session: SQLAlchemy database session

    Example:
        @app.post("/users")
        def create_user(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Initialize database tables."""
    Base.metadata.create_all(bind=engine)

