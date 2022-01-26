FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "pytest", "-q", "--no-summary", "--no-header" ]
CMD [ "tests/test_api_dashboard.py" ]
