# # def get_schemes(category=None):
# #     schemes = [
# #         {"name": "Pension Scheme", "ministry": "Social Welfare", "description": "Scheme for senior citizens.", "eligibility_rules": "Age above 18 and income below 50k", "benefits": "Monthly pension", "required_documents": "ID Proof", "official_apply_link": "https://example.com/pension", "category": "Senior Citizen"}
# #     ]
# #     if category:
# #         schemes = [scheme for scheme in schemes if scheme["category"] == category]
# #     return schemes
# import sqlite3

# def get_schemes(category=None):
#     conn = sqlite3.connect('database/schemes.db')
#     cursor = conn.cursor()
#     if category:
#         cursor.execute("SELECT * FROM schemes WHERE category=?", (category,))
#     else:
#         cursor.execute("SELECT * FROM schemes")
#     schemes = cursor.fetchall()
#     conn.close()
#     return schemes
from sqlalchemy.orm import Session
from backend.modals.scheme import Scheme

def seed_schemes(db: Session):
    if db.query(Scheme).count() > 0:
        return  # already seeded, skip

    sample_schemes = [
        Scheme(name="PM Kisan Samman Nidhi", ministry="Agriculture",
               description="Income support for farmers", category="farmer",
               min_age=18, max_income=None, gender="any",
               caste_category="any", occupation="farmer", state="any",
               benefits="Rs 6000/year in 3 installments",
               documents_required="Aadhaar, land records, bank passbook",
               apply_link="https://pmkisan.gov.in"),
        Scheme(name="Sukanya Samriddhi Yojana", ministry="Finance",
               description="Savings scheme for girl child", category="women",
               min_age=0, max_age=10, gender="female",
               caste_category="any", occupation="any", state="any",
               benefits="High interest savings account",
               documents_required="Birth certificate, Aadhaar",
               apply_link="https://www.india.gov.in/sukanya-samriddhi-yojana"),
        # add ~28 more here
    ]
    db.add_all(sample_schemes)
    db.commit()

def get_all_schemes(db: Session):
    return db.query(Scheme).all()