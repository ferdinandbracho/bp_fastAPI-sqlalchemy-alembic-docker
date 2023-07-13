from fastapi import APIRouter

from app.api.api_v1.endpoints import <dummy>


# from app.deps import PROTECTED

api_router = APIRouter()
api_router.include_router(
    <dummy>.router,
    tags=["<dummy>"],
)