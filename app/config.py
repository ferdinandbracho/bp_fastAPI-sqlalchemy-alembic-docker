import logging
import pathlib
from typing import Any, Optional

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Determine the project root directory to reliably find the .env file
# This assumes config.py is in a subdirectory of the project root (e.g., app/config.py) # noqa: E501
# Adjust if your structure is different.
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE_PATH = PROJECT_ROOT / ".env"


class Settings(BaseSettings):
    # Pydantic settings configuration
    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,  # Load from .env file at project root
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra fields not defined in the model
    )

    # Project Meta
    PROJECT_NAME: str = "UV-Powered FastAPI Boilerplate"

    # Database Configuration
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: str = "5432"  # Default PostgreSQL port
    DB_NAME: str
    # DATABASE_URL will be assembled by the validator below
    # It's Optional here because it's constructed, not directly loaded
    DATABASE_URL: Optional[PostgresDsn] = None

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(
        cls, v: Optional[str], info: ValidationInfo
    ) -> Any:
        if isinstance(
            v, str
        ):  # If DATABASE_URL is already explicitly set in .env
            return v

        # Get values from the .env file or defaults
        values = info.data
        required_keys = ["DB_USER", "DB_PASS", "DB_HOST", "DB_PORT", "DB_NAME"]
        if not all(values.get(key) for key in required_keys):
            # Get a temp logger instance or use print for early config issues
            temp_logger = logging.getLogger(__name__)
            temp_logger.warning(
                "Critical database configuration variables are missing in .env."
                "Cannot construct DATABASE_URL."
            )
            # Pydantic will still raise ValidationError for individually missing *required* root fields. # noqa: E501
            # This part of the validator is for the case where DATABASE_URL itself isn't set, # noqa: E501
            # and we are trying to build it from components.
            return None

        return PostgresDsn.build(
            scheme="postgresql+psycopg2",  # Keep this, will change to asyncpg later for async # noqa: E501
            username=values.get("DB_USER"),
            password=values.get("DB_PASS"),
            host=values.get("DB_HOST"),
            port=int(values.get("DB_PORT")),  # Ensure port is an int
            path=f"/{values.get('DB_NAME') or ''}",
        )

    # Example Configuration (optional fields)
    EXAMPLE_URL: Optional[str] = None
    EXAMPLE_QUEUE_USERS: Optional[str] = None
    EXAMPLE_ERROR: Optional[str] = None

    # Logging Configuration
    LOG_LEVEL: str = "INFO"

    def get_logger(self, name: str) -> logging.Logger:
        """Configures and returns a logger instance."""
        logger = logging.getLogger(name)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        if (
            not logger.handlers
        ):  # Avoid adding multiple handlers if called multiple times
            logger.addHandler(handler)
        logger.setLevel(self.LOG_LEVEL.upper())

        # Consider adding a FileHandler like you had before if needed
        # file_handler = logging.FileHandler(PROJECT_ROOT / "app.log")
        # file_handler.setFormatter(formatter)
        # logger.addHandler(file_handler)

        return logger


# Create a single instance of the settings to be used throughout the application
settings = Settings()

# Example: Get a logger for the current module (config.py)
# You can get loggers in other modules similarly: from app.config import settings; logger = settings.get_logger(__name__) # noqa: E501
# logger = settings.get_logger(__name__)
# logger.info("Configuration loaded successfully.")
# if settings.DATABASE_URL:
#     logger.info(f"Database URL: {settings.DATABASE_URL}")
# else:
#     logger.warning("DATABASE_URL could not be constructed. Check .env file and DB settings.") # noqa: E501
