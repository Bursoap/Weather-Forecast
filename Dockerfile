FROM python:3.7-alpine

RUN mkdir /backend
COPY ./ /backend
WORKDIR /backend

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000