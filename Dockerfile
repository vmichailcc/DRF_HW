FROM python:3.10
LABEL version="1.0"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /workspace
WORKDIR /workspace

COPY . /workspace

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

