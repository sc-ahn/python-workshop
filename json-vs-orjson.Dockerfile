FROM python:3.10.14-bullseye

ENV POETRY_VERSION=1.7.1 POETRY_HOME=/poetry
ENV PATH=/poetry/bin:$PATH
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /d3fau1t/workshop
COPY json-vs-orjson /d3fau1t/workshop
RUN poetry install --no-interaction --no-ansi
