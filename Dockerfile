FROM python:3.11-slim

WORKDIR /social_network_fastapi

COPY ./requirements.txt /social_network_fastapi/requirements.txt

RUN pip install --no-cache-dir -r /social_network_fastapi/requirements.txt

COPY . /social_network_fastapi
