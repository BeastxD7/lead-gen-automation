"""
API Key management routes.
Admin endpoints: /admin/keys/*
User endpoints: /me, /me/usage
"""
from fastapi import APIRouter, Depends
from typing import List

from app.middleware.auth import get_api_key, require_admin
from app.models.api_key import (
    APIKeyCreate,
    APIKeyData,
)
from app.db import (
    create_api_key,
    get_api_key_by_id,
    list_api_keys,
    revoke_api_key,
    delete_api_key,
    get_usage_stats
)
from app.helpers import api_success, api_error

router = APIRouter(tags=["API Keys"])


# ============== Admin Endpoints ==============

@router.post("/admin/keys")
async def create_key(
    request: APIKeyCreate,
    _: bool = Depends(require_admin)
):
    """
    Create a new API key. Admin only.
    The key value is only returned once - store it securely!
    """
    result = create_api_key(
        name=request.name,
        tier=request.tier,
        expires_in_days=request.expires_in_days
    )
    return api_success("API key created successfully", result, status_code=201)


@router.get("/admin/keys")
async def list_keys(_: bool = Depends(require_admin)):
    """List all API keys (masked). Admin only."""
    keys = list_api_keys()
    return api_success("API keys retrieved", keys)


@router.get("/admin/keys/{key_id}")
async def get_key(key_id: int, _: bool = Depends(require_admin)):
    """Get details of a specific API key. Admin only."""
    key = get_api_key_by_id(key_id)
    if not key:
        return api_error("API key not found", status_code=404)
    return api_success("API key retrieved", key)


@router.get("/admin/keys/{key_id}/usage")
async def get_key_usage(key_id: int, _: bool = Depends(require_admin)):
    """Get usage statistics for a specific API key. Admin only."""
    key = get_api_key_by_id(key_id)
    if not key:
        return api_error("API key not found", status_code=404)
    
    stats = get_usage_stats(key_id)
    return api_success("Usage stats retrieved", stats)


@router.delete("/admin/keys/{key_id}")
async def delete_key(key_id: int, _: bool = Depends(require_admin)):
    """
    Permanently delete an API key. Admin only.
    Use with caution - this cannot be undone!
    """
    success = delete_api_key(key_id)
    if not success:
        return api_error("API key not found", status_code=404)
    return api_success(f"API key {key_id} deleted")


@router.post("/admin/keys/{key_id}/revoke")
async def revoke_key(key_id: int, _: bool = Depends(require_admin)):
    """
    Revoke (deactivate) an API key. Admin only.
    The key will remain in the database but won't work.
    """
    success = revoke_api_key(key_id)
    if not success:
        return api_error("API key not found", status_code=404)
    return api_success(f"API key {key_id} revoked")


# ============== User Self-Service Endpoints ==============

@router.get("/me")
async def get_my_info(api_key: APIKeyData = Depends(get_api_key)):
    """Get your own API key info."""
    key = get_api_key_by_id(api_key.id)
    if not key:
        return api_error("API key not found", status_code=404)
    return api_success("Your API key info", key)


@router.get("/me/usage")
async def get_my_usage(api_key: APIKeyData = Depends(get_api_key)):
    """Get your own usage statistics."""
    stats = get_usage_stats(api_key.id)
    return api_success("Your usage stats", stats)
