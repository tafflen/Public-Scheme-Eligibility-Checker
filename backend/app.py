from fastapi import FastAPI, HTTPException
from backend.services.eligibility_service import check_eligibility
from backend.services.scheme_service import get_schemes

app = FastAPI()

@app.post("/register/")
async def register(user_data):
    return {"message": "User registered successfully"}

@app.post("/check-eligibility/")
async def check_eligibility_route(user_data):
    eligibility_result = check_eligibility(user_data)
    if not eligibility_result:
        raise HTTPException(status_code=400, detail="User is not eligible for any schemes")
    return {"schemes": eligibility_result}

@app.get("/schemes/")
async def get_schemes_route(category=None):
    schemes = get_schemes(category)
    return {"schemes": schemes}
