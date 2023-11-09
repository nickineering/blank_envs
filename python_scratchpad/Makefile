SHELL=/bin/bash

all: run

# Run the application locally
run:
	poetry run python src/main.py

# Run tests
test:
	poetry run mypy src/main.py && poetry run pytest

# Prepare for first run
configure:
	poetry install && cp src/.env.example src/.env && echo "Please edit src/.env file with your credentials"
