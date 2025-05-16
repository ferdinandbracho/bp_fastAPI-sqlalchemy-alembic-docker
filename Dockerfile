# Base
FROM python:3.11

# Set working directory
WORKDIR /code

# copy pyproject.toml and install dependencies
COPY ./pyproject.toml /code/pyproject.toml
RUN pip install uv
RUN uv pip install --system --no-cache-dir .

# Copy FastAPI application
COPY ./app /code/app

# Set command to run the application
CMD ["uvicorn", "app.main:app", "--reload", "--workers", "3", "--host", "0.0.0.0", "--port", "8000"]
