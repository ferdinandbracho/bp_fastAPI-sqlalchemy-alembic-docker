# FastAPI Micro-Service Boiler-Plate

This repository offers boilerplate code for initiating a [Dockerized](https://www.docker.com/)  [FastAPI](https://fastapi.tiangolo.com/)-[PostgreSQL](https://www.postgresql.org/?&)-[SQLAlchemy](https://www.sqlalchemy.org/)-[Alembic](https://alembic.sqlalchemy.org/en/latest/) project. It includes a [pre-commit](https://pre-commit.com/) framework configured with [mypy](https://mypy.readthedocs.io/en/stable/index.html) and [ruff](https://beta.ruff.rs/docs/) to ensure consistent code formatting and strict typing. Whether you're building microservices or a larger application, this template streamlines your project setup, allowing you to focus on developing your FastAPI-based microservices with confidence

Use this template as a starting point to quickly set up a robust and scalable FastAPI project with PostgreSQL, taking advantage of powerful features like automatic API documentation generation, asynchronous capabilities, and containerization for easy deployment.

### Required


## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Documentation](#documentation)
- [Contributing](#contributing)
---


## Features
- FastAPI framework for building high-performance APIs
- PostgreSQL database integration with SQLAlchemy for efficient data management
- Alembic for seamless database schema migrations
- Pre-commit framework with MyPy and ruff for code formatting and strict typing checks
- CRUD base class fot instance with needed model
- Project config file fo ease update configurations
- Utils function in utils.py (client and consumer for RabbitMQ broker for example)


Get started with your FastAPI project in no time using this template repository!


## Usage
**Initial Setup**

- Init project:
    - create and activate a [virtual env](https://docs.python.org/3/library/venv.html#module-venv)
    - install initial dependencies
    - install pre-commit config and run in all file to initial check
Positioning in the project root run make the following make command:
```sh
    make init
```
## Environment Variables
**Local Development**

To set up environment variables for local development, follow these steps:

1. Create a `.env` file in the root directory of your project.
2. Add the necessary environment variables to the .env file in the format KEY=VALUE. Adjust the [config.py](config.py) file to insert these variables into the config class instance.

Example .env file:
```txt
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASSWORD=mypassword
```

**Deployed**

For deployment, you'll need to set up environment variables or secrets in your GitHub repository. Here's how to do it:

1. Create the required environment variables or secrets in your GitHub repository.
2. In the [github-actions workflow file](.github/workflows/deploy_dev.yml) locate the env section.
3. Insert the environment variables or secrets into the workflow step, providing the necessary values.

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
The service is built is based on the [fastAPI MS Template](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker). For comprehensive technical details, instructions on how to run, deploy, and any other related considerations, please refer to the documentation provided in the [template repository](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker).
```
### 2 Indeed Information

Towards the end of your README, just before the "Contributing" section (if applicable), add links to specific sections of the template repository for Indeed Information:

```markdown
  ## Indeed Information
  For detailed information on installation and prerequisites, please refer to the [template repository](https://github.com/ferdinandbracho/bp_fastAPI-sqlalchemy-alembic-docker).
```

## **Contributing**

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes.
4. Write or update tests as necessary.
5. Submit a pull request against the main branch.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.
