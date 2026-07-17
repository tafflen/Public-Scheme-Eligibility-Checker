# def check_eligibility(user_data):
#     # Placeholder logic for eligibility checking
#     if user_data.income < 50000 and user_data.age > 18:
#         return ["Pension Scheme"]
#     return []


from sqlalchemy.orm import Session
from backend.modals.scheme import Scheme

def check_eligibility(db: Session, user_data: dict):
    schemes = db.query(Scheme).all()
    eligible, partial, not_eligible = [], [], []

    for s in schemes:
        reasons = []
        match = True

        if s.min_age is not None and user_data.get("age", 0) < s.min_age:
            match = False; reasons.append(f"Age below {s.min_age}")
        if s.max_age is not None and user_data.get("age", 0) > s.max_age:
            match = False; reasons.append(f"Age above {s.max_age}")
        if s.max_income is not None and user_data.get("annual_income", 0) > s.max_income:
            match = False; reasons.append(f"Income exceeds {s.max_income}")
        if s.gender != "any" and s.gender != user_data.get("gender"):
            match = False; reasons.append("Gender mismatch")
        if s.occupation != "any" and s.occupation != user_data.get("occupation"):
            match = False; reasons.append("Occupation mismatch")

        result = {
            "scheme": s.name,
            "benefits": s.benefits,
            "apply_link": s.apply_link,
            "reasons": reasons
        }
        if match:
            eligible.append(result)
        elif len(reasons) <= 1:
            partial.append(result)
        else:
            not_eligible.append(result)

    return {"eligible": eligible, "partial": partial, "not_eligible": not_eligible}