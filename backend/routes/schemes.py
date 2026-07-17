# from fastapi import APIRouter, Depends
# from backend.models.user import User
# from backend.services.scheme_service import get_schemes

# router = APIRouter()

# @router.get("/schemes/")
# async def get_schemes_route(category=None):
#     schemes = get_schemes(category)
#     return {"schemes": schemes}

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.services.scheme_service import get_all_schemes

router = APIRouter()

@router.get("/schemes")
def list_schemes(db: Session = Depends(get_db)):
    return get_all_schemes(db)