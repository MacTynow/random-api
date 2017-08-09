FROM python:3-alpine

RUN hug -f main.py

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -f requirements.txt
COPY . .
