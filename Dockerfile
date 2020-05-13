FROM python:3.8.2-slim

RUN mkdir /app

WORKDIR /app

# install opencv-python dependencies
RUN apt-get -y update
RUN apt-get -y install build-essential
RUN apt-get -y install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# install python package
RUN pip install numpy opencv-python flask

EXPOSE 8080

ENV FLASK_APP /app/__init__.py