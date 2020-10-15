FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /edxconnect
WORKDIR /edxconnect
COPY requirements.txt /edxconnect/
RUN pip install -r requirements.txt
COPY . /edxconnect/

