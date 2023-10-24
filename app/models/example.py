from datetime import datetime, timezone
import uuid

from sqlalchemy import TIMESTAMP, Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base


def _get_date():
    return datetime.now(timezone.utc)


class ExampleModel(Base):
    """
    Example model

    This example model is used to show how to create a model
    in SQLAlchemy. with require columns set
    """
    __tablename__ = 'example'

    id = Column(UUID(
        as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )

    active = Column(
        Boolean,
        default=True,
        doc="Is this example active?"
    )

    created_at = Column(
        TIMESTAMP,
        default=_get_date,
        doc="When was this example created?"
    )

    last_update = Column(
        TIMESTAMP,
        default=_get_date,
        onupdate=_get_date,
        doc="When was this example last updated"
    )

    update_by = Column(String(255), doc="Who updated this example")

# Delete this file after you have created your first model