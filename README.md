# FastAPI MS Boiler-Plate

This template repository provides a boilerplate setup for building a Dockerized FastAPI project with PostgreSQL as the database backend. It incorporates SQLAlchemy for efficient database interactions and Alembic for database migrations.

The repository includes a pre-commit framework configured with mypy and ruff to ensure consistent code formatting and strict typing. This helps maintain code quality and adherence to best practices.

Use this template as a starting point to quickly set up a robust and scalable FastAPI project with PostgreSQL, taking advantage of powerful features like automatic API documentation generation, asynchronous capabilities, and containerization for easy deployment.

## Features

- FastAPI framework for building high-performance APIs
- PostgreSQL database integration with SQLAlchemy for efficient data management
- Alembic for seamless database schema migrations
- Pre-commit framework with mypy and ruff for code formatting and strict typing checks
- CRUD base class fot instance with needed model
- Project config file fo ease update configurations

Get started with your FastAPI project in no time using this template repository!

Contributions are welcome! Please submit pull requests with reviewer @ferdinandbracho or open issues for any improvements or bug fixes.

## Usage
- Create Python [virtual env](https://docs.python.org/3/library/venv.html#module-venv)
    - [how-to-setup-virtual-environments-in-python](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)


- Init project: this is install initial dependencies, install pre-commit config and run in all file to initial check: Positioning in the project root run make the following make command
```sh
    make init
```