# FROM python:3.9.14-alpine3.15
FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app
RUN apt-get -y install default-libmysqlclient-dev
RUN pip3 install -r requirements.txt