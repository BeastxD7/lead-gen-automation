"""
Tests for automation routes with authentication.
"""
import pytest


class TestAutomationAuth:
    """Tests for automation routes requiring authentication."""
    
    def test_automation_requires_auth(self, client):
        """Automation endpoint should require API key (422 for missing header)."""
        response = client.post(
            "/automation",
            json={"action": "start", "config": None}
        )
        
        # FastAPI returns 422 for missing required headers
        assert response.status_code == 422
    
    def test_automation_with_auth(self, client, user_headers):
        """Automation endpoint should work with valid API key."""
        response = client.post(
            "/automation",
            headers=user_headers,
            json={"action": "stop"}
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
    
    def test_status_requires_auth(self, client):
        """Status endpoint should require API key (422 for missing header)."""
        response = client.get("/status")
        
        assert response.status_code == 422
    
    def test_status_with_auth(self, client, user_headers):
        """Status endpoint should work with valid API key."""
        response = client.get("/status", headers=user_headers)
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] == True
    
    def test_export_requires_auth(self, client):
        """Export endpoint should require API key (422 for missing header)."""
        response = client.get("/export")
        
        assert response.status_code == 422
    
    def test_export_with_auth(self, client, user_headers):
        """Export endpoint should work with valid API key."""
        response = client.get("/export", headers=user_headers)
        
        # Should return 200 (either file or success message)
        assert response.status_code == 200


class TestAutomationResponses:
    """Tests for standardized automation responses."""
    
    def test_automation_start_error_no_config(self, client, user_headers):
        """Starting automation without config should return error."""
        response = client.post(
            "/automation",
            headers=user_headers,
            json={"action": "start", "config": None}
        )
        
        assert response.status_code == 400
        data = response.json()
        assert data["success"] == False
        assert data["error"] == True
    
    def test_automation_invalid_action(self, client, user_headers):
        """Invalid action should return error."""
        response = client.post(
            "/automation",
            headers=user_headers,
            json={"action": "invalid"}
        )
        
        assert response.status_code == 400
        data = response.json()
        assert data["success"] == False
        assert data["error"] == True
    
    def test_task_not_found(self, client, user_headers):
        """Non-existent task should return error."""
        response = client.get("/status/non-existent-task-id", headers=user_headers)
        
        assert response.status_code == 404
        data = response.json()
        assert data["success"] == False
        assert data["error"] == True
