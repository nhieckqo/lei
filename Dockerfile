FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN pip install -r /requirements.txt

RUN mkdir /lei
WORKDIR /lei
COPY . /lei

RUN adduser -D user
USER user

