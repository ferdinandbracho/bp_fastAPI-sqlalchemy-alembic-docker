# Base
FROM python:3.11

# Set working diretory
WORKDIR /code

# copy requirements.txt and install
COPY ./requirements.txt /code/requirements.txt
RUN pip install uv
RUN uv pip install --system --no-cache-dir -r /code/requirements.txt

# Copy FastAPI application
COPY ./app /code/app

# Set command to run the application
CMD ["uvicorn", "app.main:app", "--reload", "--workers", "3", "--host", "0.0.0.0", "--port", "8000"]
