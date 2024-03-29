from fastapi import APIRouter

router = APIRouter(
    prefix="/hello", tags=["Hello"]
)


@router.get("")
async def get_hello():
    return {"message": "Hello world"}
