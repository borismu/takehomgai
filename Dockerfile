FROM python:3.9-alpine

EXPOSE 8000
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

# COP
# RUN apk add --no-cache --virtual .build-deps \
#     ca-certificates gcc g++ bash linux-headers musl-dev \
#     curl-dev libressl-dev git \
#     postgresql-dev postgresql-client gettext


COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000