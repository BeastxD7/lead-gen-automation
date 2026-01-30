"""
API Key authentication models.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class APIKeyCreate(BaseModel):
    """Request model for creating a new API key."""
    name: str
    tier: str = "free"
    expires_in_days: Optional[int] = None


class APIKeyResponse(BaseModel):
    """Response model for API key creation (includes the actual key - shown once)."""
    id: int
    name: str
    key: str  # Only shown once on creation!
    key_prefix: str
    tier: str
    monthly_limit: int
    created_at: datetime
    expires_at: Optional[datetime] = None


class APIKeyInfo(BaseModel):
    """Response model for API key info (without the actual key)."""
    id: int
    name: str
    key_prefix: str
    tier: str
    monthly_limit: int
    is_active: bool
    created_at: datetime
    expires_at: Optional[datetime] = None


class APIKeyData(BaseModel):
    """Data passed to route handlers after auth validation."""
    id: int
    name: str
    tier: str
    monthly_limit: int


class UsageStats(BaseModel):
    """Response model for usage statistics."""
    api_key_id: int
    total_requests: int
    total_leads: int
    monthly_leads: int
    monthly_limit: int
    remaining_quota: str | int  # "unlimited" or number
