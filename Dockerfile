FROM python:3.9-slim

WORKDIR /cv_webpage

COPY . /cv_webpage

RUN pip install --no-cache-dir --upgrade -r requirements.txt


