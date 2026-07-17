# class Scheme:
#     def __init__(self, name, ministry, description, eligibility_rules, benefits, required_documents, official_apply_link, category):
#         self.name = name
#         self.ministry = ministry
#         self.description = description
#         self.eligibility_rules = eligibility_rules
#         self.benefits = benefits
#         self.required_documents = required_documents
#         self.official_apply_link = official_apply_link
#         self.category = category
from sqlalchemy import Column, Integer, String
from backend.database import Base

class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ministry = Column(String)
    description = Column(String)
    category = Column(String)
    min_age = Column(Integer, nullable=True)
    max_age = Column(Integer, nullable=True)
    max_income = Column(Integer, nullable=True)
    gender = Column(String, default="any")
    caste_category = Column(String, default="any")
    occupation = Column(String, default="any")
    state = Column(String, default="any")
    benefits = Column(String)
    documents_required = Column(String)
    apply_link = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    state = Column(String)
    district = Column(String)
    occupation = Column(String)
    annual_income = Column(Integer)
    education = Column(String)
    caste_category = Column(String)