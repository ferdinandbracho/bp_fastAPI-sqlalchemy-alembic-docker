from fastapi.testclient import TestClient

from app.main import app  # Import your FastAPI app instance

client = TestClient(app)

def test_health_check_endpoint():
    """Test the main health check endpoint."""
    response = client.get("/api/v1/health-check/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

def test_db_health_check_endpoint():
    """Test the database health check endpoint."""
    # This test assumes your database is accessible and configured during testing. # noqa: E501
    # For more isolated unit tests, you might mock the DB session or use a dedicated test database. # noqa: E501
    response = client.get("/api/v1/health-check/db")
    # Depending on your setup, the DB might not be running or accessible during unit tests without specific fixtures. # noqa: E501
    # If so, this test might fail with a 500 or timeout if it can't connect. # noqa: E501
    # Consider what state the DB is in when tests run. # noqa: E501
    # For now, we'll assume it's expected to work or that a more specific error is handled gracefully by the endpoint. # noqa: E501
    assert response.status_code == 200 
    # The exact message might vary if the DB isn't up. Let's be a bit flexible or assume success. # noqa: E501
    # A more robust test would check for specific error messages if the DB is down and the endpoint handles it. # noqa: E501
    assert response.json().get("message") == "Database connection: OK"
