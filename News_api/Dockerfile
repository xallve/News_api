FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /django_news_api

WORKDIR /django_news_api

COPY . .

COPY ./requirements.txt /requirements.txt

RUN apk add --update postgresql-client jpeg-dev

RUN apk add --update --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt

RUN adduser -D user

USER user