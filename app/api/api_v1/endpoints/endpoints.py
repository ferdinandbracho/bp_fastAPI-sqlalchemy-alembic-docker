from fastapi import APIRouter, status

# Init router
router = APIRouter()

#  Dummy get request. Delete this endpoint after adding your own
@router.get("/", status_code=status.HTTP_200_OK)
def dummy_get() -> str:
    """
    ## Dummy get request

    return 200
    """

    return 'Dummy get request'
