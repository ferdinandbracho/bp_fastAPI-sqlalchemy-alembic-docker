from typing import List, Optional

from pydantic import UUID4, BaseModel


class Example(BaseModel):
    """
    Example model.

    This example model is used to show how to create a Pydantic model
    with required and optional fields set.
    """

    id: Optional[UUID4] = None
    active: bool
    float_value: float
    int_value: int
    optional_value: Optional[int] = None
    list_value: List[int] = []

    class Config:
        orm_mode = True

# delete this file after you have created your first model
