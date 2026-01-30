"""
Pytest configuration and fixtures for Anvesh tests.
"""
import pytest
import os
from fastapi.testclient import TestClient

# Set test environment variables BEFORE importing the app
os.environ["ADMIN_SECRET"] = "test-admin-secret"
os.environ["DB_NAME"] = "lead_scraper_test"

from app.main import app
from app.db import create_api_key, delete_api_key
from app.db.database import get_connection, init_db


@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    """Initialize the test database once per session."""
    init_db()
    yield
    # Cleanup could go here if needed


@pytest.fixture
def client():
    """FastAPI test client."""
    return TestClient(app)


@pytest.fixture
def admin_headers():
    """Headers for admin requests."""
    return {"X-Admin-Secret": "test-admin-secret"}


@pytest.fixture
def test_api_key():
    """Create a test API key and clean up after."""
    key_data = create_api_key(name="Test Key", tier="free")
    yield key_data
    # Cleanup
    delete_api_key(key_data["id"])


@pytest.fixture
def user_headers(test_api_key):
    """Headers for authenticated user requests."""
    return {"X-API-Key": test_api_key["key"]}


@pytest.fixture
def pro_api_key():
    """Create a pro tier test API key."""
    key_data = create_api_key(name="Pro Test Key", tier="pro")
    yield key_data
    delete_api_key(key_data["id"])
