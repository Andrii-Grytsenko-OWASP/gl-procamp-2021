FROM python:3.9-slim

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./src /app/src
COPY ./tests /app/tests
COPY ./logs /app/logs

WORKDIR /app

ENTRYPOINT [ "pytest", "-q", "--no-summary", "--no-header" ]
CMD [ "/app/tests/test_api_dashboard.py" ]
