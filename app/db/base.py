# Need to import here all models
from sqlalchemy.ext.declarative import declarative_base

# Base for SQLAlchemy models
Base = declarative_base()

# Import all models here to ensure they are registered with Base
# For example:
# from app.models.user import User # noqa
# from app.models.item import Item # noqa