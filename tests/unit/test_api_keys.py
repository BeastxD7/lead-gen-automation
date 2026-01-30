"""
Tests for API key database operations.
"""
import pytest
from app.db.api_keys import (
    generate_api_key,
    create_api_key,
    validate_api_key,
    get_api_key_by_id,
    delete_api_key,
    log_usage,
    get_usage_stats
)
from config import settings


class TestAPIKeyGeneration:
    """Tests for API key generation and hashing."""
    
    def test_generate_api_key_format(self):
        """Generated key should have the correct prefix."""
        full_key, key_hash, key_prefix = generate_api_key()
        
        assert full_key.startswith(settings.api_key_prefix)
        assert len(key_hash) == 64  # SHA256 hex
        assert key_prefix == full_key[:12]
    
    def test_generate_api_key_uniqueness(self):
        """Each generated key should be unique."""
        keys = [generate_api_key()[0] for _ in range(5)]
        assert len(set(keys)) == 5


class TestAPIKeyValidation:
    """Tests for API key validation."""
    
    def test_validate_api_key_success(self):
        """Valid key should return key data."""
        key_data = create_api_key(name="Validation Test", tier="free")
        
        result = validate_api_key(key_data["key"])
        
        assert result is not None
        assert result["id"] == key_data["id"]
        assert result["name"] == "Validation Test"
        assert result["tier"] == "free"
        
        # Cleanup
        delete_api_key(key_data["id"])
    
    def test_validate_api_key_invalid(self):
        """Invalid key should return None."""
        result = validate_api_key("anv_invalid_key_that_does_not_exist")
        assert result is None
    
    def test_validate_api_key_empty(self):
        """Empty key should return None."""
        result = validate_api_key("")
        assert result is None


class TestUsageLogging:
    """Tests for usage logging and statistics."""
    
    def test_log_usage(self):
        """Usage should be logged correctly."""
        key_data = create_api_key(name="Usage Test", tier="free")
        
        log_usage(key_data["id"], "/test-endpoint", 5)
        log_usage(key_data["id"], "/test-endpoint", 3)
        
        stats = get_usage_stats(key_data["id"])
        
        assert stats["total_requests"] >= 2
        assert stats["total_leads"] >= 8
        
        # Cleanup
        delete_api_key(key_data["id"])
    
    def test_get_usage_stats_empty(self):
        """New key should have zero usage."""
        key_data = create_api_key(name="Empty Stats Test", tier="pro")
        
        stats = get_usage_stats(key_data["id"])
        
        assert stats["total_requests"] == 0
        assert stats["total_leads"] == 0
        assert stats["monthly_leads"] == 0
        
        # Cleanup
        delete_api_key(key_data["id"])
