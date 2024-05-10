import pytest
from predictions import app
import json

@pytest.fixture()
def client():
    return app.test_client()

def test_pinger(client):
    result = client.get("/ping")
    assert result.status_code == 200
    assert result.json == {"MESSAGE": "Hi I am pinging V2...."}

def test_predict(client):
    test_data= {
    "Gender": "Male",
    "Married": "Yes",
    "ApplicantIncome": 500,
    "LoanAmount": 50000000,
    "Credit_History": 1.0
}
    result = client.post('/predict', json= test_data)

    assert result.status_code == 200
    assert result.json == {
    "loan_approval_status": "Rejected"}