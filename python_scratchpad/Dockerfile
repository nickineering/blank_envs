# Simple starter Dockerfile for a Python project using Poetry

FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root
CMD ["poetry", "run", "python", "src/main.py"]
