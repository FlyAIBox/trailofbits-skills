"""SQLAlchemy database models."""

from sqlalchemy import Column, Integer, LargeBinary, String

from .database import Base


class User(Base):
    """User model for registration and authentication."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(LargeBinary, nullable=False)

    def __repr__(self) -> str:
        """String representation of User."""
        return f"<User(id={self.id}, username={self.username!r})>"

