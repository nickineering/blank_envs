SHELL=/bin/bash

all: run

# Prepare for first run
configure:
	poetry install
	cp src/.env.example src/.env
	echo "Please edit src/.env file with your credentials"

# Run the application locally
run:
	poetry run python src/main.py

# Run tests
test:
	poetry run pytest

# Check types
types:
	poetry run mypy src/

lint:
	poetry run ruff format && poetry run ruff check --fix
