FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE app.settings

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN adduser -D user
USER user