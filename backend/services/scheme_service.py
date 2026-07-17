def get_schemes(category=None):
    schemes = [
        {"name": "Pension Scheme", "ministry": "Social Welfare", "description": "Scheme for senior citizens.", "eligibility_rules": "Age above 18 and income below 50k", "benefits": "Monthly pension", "required_documents": "ID Proof", "official_apply_link": "https://example.com/pension", "category": "Senior Citizen"}
    ]
    if category:
        schemes = [scheme for scheme in schemes if scheme["category"] == category]
    return schemes
