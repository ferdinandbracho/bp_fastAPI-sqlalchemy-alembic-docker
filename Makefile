.PHONY: help init lint format test run docker-build docker-run alembic-revision alembic-upgrade clean

# Default command: Display help
help:
	@echo "Available commands:"
	@echo "  help                 Show this help message"
	@echo "  init                 Initialize the project (create venv, install deps, pre-commit)"
	@echo "  lint                 Run linters and style checks via pre-commit"
	@echo "  format               Format code using ruff"
	@echo "  test                 Run tests using pytest"
	@echo "  run                  Run the FastAPI development server with Uvicorn"
	@echo "  docker-build         Build the Docker image"
	@echo "  docker-run           Run the application in a Docker container"
	@echo "  alembic-revision     Create a new Alembic database migration. Usage: make alembic-revision MSG=\"your message\""
	@echo "  alembic-upgrade      Apply database migrations to the 'head'"
	@echo "  clean                Remove temporary files and build artifacts"

init:
	python3 -m venv venv && . venv/bin/activate && pip install uv && uv pip install --no-cache-dir ".[dev]" && pre-commit install && pre-commit run --all-files

lint:
	@echo "Running linters and style checks..."
	uv run pre-commit run --all-files

format:
	@echo "Formatting code..."
	uv run ruff format .

test:
	@echo "Running tests..."
	uv run pytest

run:
	@echo "Starting FastAPI development server..."
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

docker-build:
	@echo "Building Docker image..."
	docker build -t bp-fastapi-sqlalchemy-alembic-docker .

docker-run:
	@echo "Running Docker container..."
	docker run -d -p 8000:8000 --env-file .env --name bp-fastapi-app bp-fastapi-sqlalchemy-alembic-docker

# Example: make alembic-revision MSG="create_users_table"
MSG ?= "new_migration"
alembic-revision:
	@echo "Creating Alembic revision: $(MSG)"
	uv run alembic revision -m "$(MSG)"

alembic-upgrade:
	@echo "Applying Alembic migrations..."
	uv run alembic upgrade head

clean:
	@echo "Cleaning up..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -rf .pytest_cache .mypy_cache .ruff_cache build/ dist/ *.egg-info/ venv/ .venv/
	@echo "Clean up complete."