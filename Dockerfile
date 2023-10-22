FROM python:3.11
ENV PYTHONBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/
