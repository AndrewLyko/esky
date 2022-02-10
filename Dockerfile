FROM python:3.10.2 AS build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_CODE=/usr/src/app

WORKDIR $APP_CODE

COPY Pipfile Pipfile.lock $APP_CODE/

RUN python -m pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --system

COPY . $APP_CODE/

FROM build AS development
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000

EXPOSE 8000
