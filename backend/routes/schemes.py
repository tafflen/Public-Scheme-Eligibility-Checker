from fastapi import APIRouter, Depends
from backend.models.user import User
from backend.services.scheme_service import get_schemes

router = APIRouter()

@router.get("/schemes/")
async def get_schemes_route(category=None):
    schemes = get_schemes(category)
    return {"schemes": schemes}
