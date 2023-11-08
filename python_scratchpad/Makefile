SHELL=/bin/bash

all: run

# Run the application locally
run:
	poetry run python main.py

# Run tests
test:
	poetry run mypy main.py && poetry run pytest
