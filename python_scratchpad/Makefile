SHELL=/bin/bash

all: run

# Run the application locally
run:
	poetry run python src/main.py

# Run tests
test:
	poetry run mypy src/main.py && poetry run pytest
