from fastapi import APIRouter


router = APIRouter()


@router.get("", summary="Привет мир")
async def hello_world():
    return {"message": "Привет, мир!"}
