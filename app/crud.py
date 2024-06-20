from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.session import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD)
        **Parameters**
        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        """
        Get a single object by ID
        **Parameters**
        * `db`: SQLAlchemy database session
        * `id`: The object ID
        **Returns**
        * The object with matching ID if found, otherwise `None`

        """

        return db.query(self.model).filter(self.model.id == id).first()

    def get_coincidence(self, db: Session, **kwargs) -> Optional[ModelType]:
        """
        Get a single object by coincidence
        **Parameters**
        * `db`: SQLAlchemy database session
        * `kwargs`: The object coincidence
        **Returns**
        * The object with matching ID if found, otherwise `None`

        """

        return db.query(self.model).filter_by(**kwargs).first()

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 0
    ) -> List[ModelType]:
        """
        Get multiple objects
        **Parameters**
        * `db`: SQLAlchemy database session
        * `skip`: The number of objects to skip
        * `limit`: Maximum number of objects to return
        **Returns**
        * A list of objects

        """

        return db.query(self.model).offset(skip).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """
        Create an object
        **Parameters**
        * `db`: SQLAlchemy database session
        * `obj_in`: Pydantic model for create
        **Returns**
        * The object that was created

        """

        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        """
        Update an object
        **Parameters**
        * `db`: SQLAlchemy database session
        * `db_obj`: The object to update
        * `obj_in`: Pydantic model or dict with new data
        **Returns**
        * The object that was updated

        """

        obj_data = jsonable_encoder(db_obj)

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: UUID) -> ModelType:
        """
        Remove an object
        **Parameters**
        * `db`: SQLAlchemy database session
        * `id`: The object ID
        **Returns**
        * The object that was deleted

        """

        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def soft_remove(self, db: Session, *, id: UUID) -> ModelType:
        """
        Soft remove an object
        **Parameters**
        * `db`: SQLAlchemy database session
        * `id`: The object ID
        **Returns**
        * The object that was soft deleted

        """

        obj = db.query(self.model).get(id)
        obj.is_active = False
        db.add(obj)
        db.commit()
        return obj
