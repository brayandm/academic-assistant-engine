FROM python:3.11.3-alpine3.18

RUN pip install pipenv

COPY . /app

WORKDIR /app

RUN pipenv install