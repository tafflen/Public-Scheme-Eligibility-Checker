# from fastapi import APIRouter, Depends
# from backend.models.user import User
# from backend.services.eligibility_service import check_eligibility

# router = APIRouter()

# @router.post("/check-eligibility/")
# async def check_eligibility_route(user_data: User):
#     eligibility_result = check_eligibility(user_data)
#     if not eligibility_result:
#         raise HTTPException(status_code=400, detail="User is not eligible for any schemes")
#     return {"schemes": eligibility_result}


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.services.eligibility_service import check_eligibility

router = APIRouter()

@router.post("/check-eligibility")
def eligibility_endpoint(user_data: dict, db: Session = Depends(get_db)):
    return check_eligibility(db, user_data)