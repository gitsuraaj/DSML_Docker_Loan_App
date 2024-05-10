FROM python:3.9.6-slim-buster
WORKDIR /Users/suraaj/Desktop/DSML_Docker_Loan_App/DOCKER

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY  . .
CMD ["python3", "-m", "flask", "--app", "predictions.py", "run", "--host=0.0.0.0"]

#docker build -t loan_app_flask_v1 .
#docker run -p 8000:5000 loan_app_flask_v1

#docker login -u suraajscaler


