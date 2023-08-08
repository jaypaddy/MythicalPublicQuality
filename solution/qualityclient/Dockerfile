FROM amd64/python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/env.py .
COPY app/main.py .
COPY app/JSONFormatter.py .
COPY app/metrics.py .
COPY app/logging.conf .


CMD [ "python3", "-u", "./main.py" ]