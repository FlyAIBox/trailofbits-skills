"""Application configuration using Pydantic settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str = "postgresql://user:password@localhost:5432/userdb"

    # JWT
    secret_key: str  # Must be set in environment (no default for security)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # bcrypt
    bcrypt_rounds: int = 12

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Global settings instance
settings = Settings()

# Security validation
if len(settings.secret_key) < 32:
    msg = "SECRET_KEY must be at least 32 characters"
    raise ValueError(msg)

