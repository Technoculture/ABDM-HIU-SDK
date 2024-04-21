FROM python:3.12

WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=1.7.1

EXPOSE 8000

COPY ["pyproject.toml", "poetry.lock", "./"]

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -




COPY . .

RUN poetry install --no-interaction --no-ansi


CMD ["uvicorn", "server:app", "--port", "8000", "--host", "0.0.0.0", "--reload"]