# UV-Powered FastAPI Micro-Service Boilerplate

[![Python Version](https://img.shields.io/badge/python-%3E%3D3.13-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-purple.svg)](https://github.com/astral-sh/ruff)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker/deploy_dev.yml?branch=main&logo=githubactions)](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker/actions/workflows/deploy_dev.yml?query=branch%3Amain)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

This repository offers boilerplate code for initiating a UV-managed, [Dockerized](https://www.docker.com/) [FastAPI](https://fastapi.tiangolo.com/)-[PostgreSQL](https://www.postgresql.org/?&)-[SQLAlchemy](https://www.sqlalchemy.org/)-[Alembic](https://alembic.sqlalchemy.org/en/latest/) project. It includes a [pre-commit](https://pre-commit.com/) framework configured with [mypy](https://mypy.readthedocs.io/en/stable/index.html) and [ruff](https://beta.ruff.rs/docs/) to ensure consistent code formatting and strict typing. Whether you're building microservices or a larger application, this template streamlines your project setup, allowing you to focus on developing your FastAPI-based microservices with confidence using `uv` for package management.

Use this template as a starting point to quickly set up a robust and scalable FastAPI project with PostgreSQL, taking advantage of powerful features like automatic API documentation generation, asynchronous capabilities, and containerization for easy deployment.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Features

- FastAPI framework for building high-performance APIs
- PostgreSQL database integration with SQLAlchemy for efficient data management
- Alembic for seamless database schema migrations
- Pre-commit framework with MyPy and ruff for code formatting and strict typing checks
- CRUD base class for instance with needed model
- Project config file for ease of update configurations
- Utils function in utils.py (client and consumer for RabbitMQ broker for example)

Get started with your FastAPI project in no time using this template repository!

## Usage

### Initial Setup

This project uses `uv` for package and environment management.

1. **Ensure `uv` is installed**: If you don't have `uv` installed, follow the instructions at [astral.sh/uv/install](https://astral.sh/uv/install).

1. **Create and Activate Virtual Environment**: Navigate to the project root and run:

   ```sh
   uv venv
   source .venv/bin/activate
   ```

   This creates a virtual environment in `.venv/` and activates it.

1. **Install Dependencies**: With the virtual environment active, install the project dependencies (including development tools like `pre-commit` and `pytest`):

   ```sh
   uv sync --all-extras
   ```

   Alternatively, you can use `uv pip install ".[dev]"`.

1. **Install Pre-commit Hooks**: To ensure code quality and consistency, install the pre-commit hooks:

   ```sh
   pre-commit install
   ```

   This will run linters and formatters automatically before each commit. You can also run them manually on all files:

   ```sh
   pre-commit run --all-files
   ```

### Alternative Setup with `make`

A `Makefile` is provided with an `init` target that automates the above steps. It will create a virtual environment named `venv` (note: not `.venv`), install `uv` into it if necessary, install dependencies, and set up pre-commit. Positioning in the project root run the following make command:

```sh
make init
```

### Makefile Commands

The project includes a `Makefile` to streamline common development tasks. Here are the available commands:

- `make help`: Displays a list of all available `make` commands and their descriptions.
- `make init`: Initializes the project. This includes creating a Python virtual environment in `venv/`, installing `uv` (if not present in the environment's pip), installing all project dependencies using `uv pip install ".[dev]"`, installing pre-commit hooks, and running pre-commit on all files.
- `make lint`: Runs linters and style checks using `pre-commit run --all-files`.
- `make format`: Formats the codebase using `ruff format .`.
- `make test`: Executes the test suite using `pytest` (via `uv run pytest`).
- `make run`: Starts the FastAPI development server using Uvicorn on `http://0.0.0.0:8000` with live reloading (`uv run uvicorn app.main:app --reload`).
- `make docker-build`: Builds the Docker image for the application, tagging it as `bp-fastapi-sqlalchemy-alembic-docker`.
- `make docker-run`: Runs the application in a Docker container in detached mode. It maps port 8000, uses the `.env` file from the project root for environment variables, and names the container `bp-fastapi-app`.
- `make alembic-revision MSG="your_message_here"`: Creates a new Alembic database migration. The `MSG` variable is optional; if not provided, it defaults to "new_migration".
- `make alembic-upgrade`: Applies all pending Alembic database migrations, upgrading the database to the latest revision (`head`).
- `make clean`: Removes temporary files and build artifacts, including `__pycache__` directories, `*.pyc` files, test/lint caches (`.pytest_cache`, `.mypy_cache`, `.ruff_cache`), build artifacts (`build/`, `dist/`, `*.egg-info/`), and the `venv/` and `.venv/` virtual environment directories.

To use these commands, simply run them from the project's root directory (e.g., `make lint`).

### Running Tests

This project uses `pytest` for testing. To run the tests:

1. Ensure your virtual environment is activated (`source .venv/bin/activate`).
1. Run pytest:

   ```sh
   pytest
   ```

Or, using `uv run` (which doesn't require activating the venv first):

```sh
uv run pytest
```

## Environment Variables

### Local Development

To set up environment variables for local development, follow these steps:

1. Create a `.env` file in the root directory of your project.
1. Add the necessary environment variables to the .env file in the format KEY=VALUE. Adjust the [config.py](config.py) file to insert these variables into the config class instance.

Example .env file:

```txt
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASSWORD=mypassword
```

### Deployed

For deployment, you'll need to set up environment variables or secrets in your GitHub repository. Here's how to do it:

1. Create the required environment variables or secrets in your GitHub repository.
1. In the [github-actions workflow file](.github/workflows/deploy_dev.yml) locate the env section.
1. Insert the environment variables or secrets into the workflow step, providing the necessary values.

Example workflow step:

```yaml
- name: Deploy
  env:
    DB_HOST: ${{ vars.DB_HOST }}
    DB_PORT: ${{ vars.DB_PORT }}
    DB_USER: ${{ secrets.DB_USER }}
    DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
  run: |
    # Add your deployment script here
```

## Documentation

Please ensure you update this README after implementing an instance of this template. Here are the recommended steps to follow:

### 1. Introduction and Overview

In your README's "Introduction and/or Overview" section (or similar), include the following information:

```markdown
The service is built based on the [UV-Powered FastAPI MS Template](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker). For comprehensive technical details, instructions on how to run, deploy, and any other related considerations, please refer to the documentation provided in the [template repository](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker).
```

### 2. Indeed Information

Towards the end of your README, just before the "Contributing" section (if applicable), add links to specific sections of the template repository for Indeed Information:

```markdown
## Indeed Information
For detailed information on installation and prerequisites, please refer to the [UV-Powered FastAPI MS Template repository](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker).
```

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
1. Create a new branch for your feature or bug fix.
1. Implement your changes.
1. Write or update tests as necessary.
1. Submit a pull request against the main branch.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.
