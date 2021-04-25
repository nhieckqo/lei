FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV MY_PASSWORD = 'NDVSA2020'

COPY ./requirements.txt /requirements.txt
RUN apt-get update
RUN apt-get install -y postgresql
RUN apt-get install libpq-dev gcc
RUN export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-psycopg2

RUN pip3 install -r requirements.txt

RUN mkdir /lei
WORKDIR /lei
COPY . /lei

RUN adduser --disabled-password user
USER user
