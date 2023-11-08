FROM python:3.11-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip setuptools

RUN pip install -r requirements.txt

COPY . .