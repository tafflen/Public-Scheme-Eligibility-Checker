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
            # --- 5 Tamil Nadu State Schemes ---
        Scheme(name="Amma Two Wheeler Scheme", ministry="TN Social Welfare",
            description="50% subsidy on two-wheelers for working women in Tamil Nadu",
            category="women", min_age=18, max_age=45, max_income=250000,
            gender="female", caste_category="any", occupation="any", state="Tamil Nadu",
            benefits="50% subsidy up to Rs 25,000 on two-wheeler purchase",
            documents_required="Aadhaar, income certificate, driving license",
            apply_link="https://www.tn.gov.in/scheme/amma-two-wheeler"),

        Scheme(name="Thalikku Thangam Thittam", ministry="TN Social Welfare",
            description="Gold for marriage assistance scheme for TN women",
            category="women", min_age=18, max_age=None, max_income=72000,
            gender="female", caste_category="any", occupation="any", state="Tamil Nadu",
            benefits="4 grams gold or Rs 20,000 cash assistance for marriage",
            documents_required="Aadhaar, income certificate, marriage certificate",
            apply_link="https://www.tn.gov.in/scheme/thalikku-thangam"),

        Scheme(name="Pudhumai Penn Scheme", ministry="TN School Education",
            description="Monthly financial assistance for girl students in higher secondary",
            category="student", min_age=15, max_age=21, max_income=250000,
            gender="female", caste_category="any", occupation="student", state="Tamil Nadu",
            benefits="Rs 1000/month until graduation",
            documents_required="Aadhaar, income certificate, school enrollment proof",
            apply_link="https://pudhumaipenn.tnschools.gov.in"),

        Scheme(name="Chief Minister's Comprehensive Health Insurance Scheme",
            ministry="TN Health", description="Free health insurance for TN families",
            category="general", min_age=0, max_age=None, max_income=400000,
            gender="any", caste_category="any", occupation="any", state="Tamil Nadu",
            benefits="Cashless treatment up to Rs 5 lakh per family per year",
            documents_required="Aadhaar, ration card, income certificate",
            apply_link="https://www.cmchistn.com"),

        Scheme(name="Uzhavar Pathukappu Thittam (Farmer Security Scheme)",
            ministry="TN Agriculture", description="Insurance and welfare scheme for TN farmers",
            category="farmer", min_age=18, max_age=None, max_income=None,
            gender="any", caste_category="any", occupation="farmer", state="Tamil Nadu",
            benefits="Accident insurance cover and pension for farmers",
            documents_required="Aadhaar, land ownership documents",
            apply_link="https://www.tn.gov.in/scheme/uzhavar-pathukappu"),

        # --- 5 Central Government Schemes ---
        Scheme(name="Pradhan Mantri Awas Yojana", ministry="Housing and Urban Affairs",
            description="Affordable housing scheme for economically weaker sections",
            category="general", min_age=18, max_age=None, max_income=1800000,
            gender="any", caste_category="any", occupation="any", state="any",
            benefits="Interest subsidy on home loans up to Rs 2.67 lakh",
            documents_required="Aadhaar, income certificate, property documents",
            apply_link="https://pmaymis.gov.in"),

        Scheme(name="Ayushman Bharat - PMJAY", ministry="Health and Family Welfare",
            description="Health insurance scheme for economically vulnerable families",
            category="general", min_age=0, max_age=None, max_income=250000,
            gender="any", caste_category="any", occupation="any", state="any",
            benefits="Free treatment up to Rs 5 lakh per family per year",
            documents_required="Aadhaar, ration card, SECC data verification",
            apply_link="https://pmjay.gov.in"),

        Scheme(name="Pradhan Mantri Mudra Yojana", ministry="Finance",
            description="Collateral-free loans for small businesses and entrepreneurs",
            category="entrepreneur", min_age=18, max_age=None, max_income=None,
            gender="any", caste_category="any", occupation="entrepreneur", state="any",
            benefits="Loans up to Rs 10 lakh without collateral",
            documents_required="Aadhaar, business plan, bank statements",
            apply_link="https://www.mudra.org.in"),

        Scheme(name="National Old Age Pension Scheme", ministry="Rural Development",
            description="Monthly pension for senior citizens below poverty line",
            category="senior_citizen", min_age=60, max_age=None, max_income=100000,
            gender="any", caste_category="any", occupation="any", state="any",
            benefits="Rs 200-500/month pension depending on age",
            documents_required="Aadhaar, age proof, BPL certificate",
            apply_link="https://nsap.nic.in"),

        Scheme(name="Pradhan Mantri Jan Dhan Yojana", ministry="Finance",
            description="Financial inclusion scheme providing access to banking",
            category="general", min_age=10, max_age=None, max_income=None,
            gender="any", caste_category="any", occupation="any", state="any",
            benefits="Zero-balance bank account with Rs 2 lakh accident insurance",
            documents_required="Aadhaar, address proof",
            apply_link="https://www.pmjdy.gov.in"),
        # add ~28 more here
    ]
    db.add_all(sample_schemes)
    db.commit()

def get_all_schemes(db: Session):
    return db.query(Scheme).all()