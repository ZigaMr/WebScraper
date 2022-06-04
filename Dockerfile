FROM python:3.8-slim-buster

ENV POETRY_VERSION=1.1.1

RUN apt-get update \
    #&& apt-get install -y wget \
    && pip install poetry==$POETRY_VERSION 
    #&& wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    # && apt-get --assume-yes install ./google-chrome-stable_current_amd64.deb

# ENV PATH="${PATH}:/home/WebScrape/.local/bin"

COPY ./pyproject.toml pyproject.toml
COPY ./poetry.lock poetry.lock
COPY ./scraper.py scraper.py
RUN poetry config virtualenvs.create false \
    && poetry install
RUN poetry run python scraper.py


