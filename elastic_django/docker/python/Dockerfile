FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

COPY ./docker/python/requirements.txt /requirements.txt

RUN apt-get install default-libmysqlclient-dev
RUN pip install -r /requirements.txt

RUN mkdir /elastic_django
WORKDIR /elastic_django
COPY ./ /elastic_django

RUN useradd user

USER user
