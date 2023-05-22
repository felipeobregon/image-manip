FROM python:3.8-slim-buster

COPY . /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /app/server

CMD [ "gunicorn", "serve:app" ]