import pytest
from unittest.mock import MagicMock, patch
from app.db import insert_lead

# Mock lead data
mock_lead = {
    "business_name": "Test Bakery",
    "industry": "Bakery",
    "category": "Bakery",
    "location": "New York, USA",
    "address": "123 Bread St, NY",
    "rating": "4.5",
    "review_count": 100,
    "is_claimed": True,
    "has_website": True,
    "website_url": "https://testbakery.com",
    "phone": "+1234567890"
}

@patch("app.db.database.get_connection")
def test_insert_lead_success(mock_get_connection):
    """Test inserting a new lead successfully."""
    # Setup mock cursor and connection
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_get_connection.return_value.__enter__.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    
    # Mock fetchone to return a result (indicating successful insert)
    mock_cursor.fetchone.return_value = {"id": 1}
    
    result = insert_lead(mock_lead)
    
    assert result is True
    mock_cursor.execute.assert_called_once()
    
@patch("app.db.database.get_connection")
def test_insert_lead_duplicate(mock_get_connection):
    """Test inserting a duplicate lead (should return False)."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    
    mock_get_connection.return_value.__enter__.return_value = mock_conn
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    
    # Mock fetchone to return None (indicating duplicate/no insert)
    mock_cursor.fetchone.return_value = None
    
    result = insert_lead(mock_lead)
    
    assert result is False
