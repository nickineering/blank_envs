SHELL=/bin/bash

all: run

# Prepare for first run
setup:
	poetry install
	poetry run update-ruff-base
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
	poetry run pyright src/

# Lint and format the code
lint:
	poetry run ruff format && poetry run ruff check --fix
