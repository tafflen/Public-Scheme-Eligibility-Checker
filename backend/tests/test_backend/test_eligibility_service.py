from backend.services.eligibility_service import check_eligibility

def test_check_eligibility():
    user_data = {
        "income": 50000,
        "age": 18,
        "occupation": "",
        "annualIncome": "",
        "education": "",
        "category": "",
        "disabilityStatus": ""
    }
    result = check_eligibility(user_data)
    assert len(result) == 1
    assert result[0] == "Pension Scheme"
