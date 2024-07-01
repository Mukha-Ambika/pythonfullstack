"""
This module contains integration tests for the Sharbo API.

The integration tests in this module are used to test the functionality of the API endpoints
by making actual requests to the API and asserting the responses.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    """
    Test case for the read_root function.

    This function sends a GET request to the root endpoint ("/") and asserts that the response
    status code is 200 and the JSON response body is equal to {"message": "Welcome to Sharbo!"}.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Sharbo!"}
