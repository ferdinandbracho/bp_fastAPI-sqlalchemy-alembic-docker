from typing import Any, Dict

from fastapi import APIRouter, status

from app.config import settings

router = APIRouter()
logger = settings.get_logger(__name__)


# health check
@router.get("/health-check", status_code=status.HTTP_200_OK)
def health_check() -> Dict[Any, Any]:
    """
    ## Ping base Health checker

    return 200
    """

    return {'message': 'Users - service active'}
