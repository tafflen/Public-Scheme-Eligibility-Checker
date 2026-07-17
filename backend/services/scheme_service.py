# def get_schemes(category=None):
#     schemes = [
#         {"name": "Pension Scheme", "ministry": "Social Welfare", "description": "Scheme for senior citizens.", "eligibility_rules": "Age above 18 and income below 50k", "benefits": "Monthly pension", "required_documents": "ID Proof", "official_apply_link": "https://example.com/pension", "category": "Senior Citizen"}
#     ]
#     if category:
#         schemes = [scheme for scheme in schemes if scheme["category"] == category]
#     return schemes
import sqlite3

def get_schemes(category=None):
    conn = sqlite3.connect('database/schemes.db')
    cursor = conn.cursor()
    if category:
        cursor.execute("SELECT * FROM schemes WHERE category=?", (category,))
    else:
        cursor.execute("SELECT * FROM schemes")
    schemes = cursor.fetchall()
    conn.close()
    return schemes
