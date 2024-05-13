from flask import Flask, request
import pickle
import sklearn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Scaler V4 !</p>"


@app.route("/ping")
def pinger():
    return {"MESSAGE": "Hi I am pinging V2...."}

model_pickle= open("artefacts/classifier.pkl", 'rb')
clf = pickle.load(model_pickle)

@app.route("/predict", methods=['POST'])
def predict():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        gender = 0
    else:
        gender = 1

    if loan_req['Married'] == "No":
        married = 0
    else:
        married = 1

    applicant_income = loan_req['ApplicantIncome']
    credit_history = loan_req['Credit_History']
    loan_amount = loan_req['LoanAmount']

    input_data = [[gender, married, applicant_income,loan_amount , credit_history]]
    prediction = clf.predict(input_data)

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Accepted"

    return {"loan_approval_status": pred}

