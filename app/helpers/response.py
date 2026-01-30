"""
Standardized API Response Helpers.

Provides uniform response structure across all API endpoints:
{
    "success": true/false,
    "message": "Human readable message",
    "data": {...} or null,
    "error": false/true
}
"""
from fastapi import status
from fastapi.responses import JSONResponse
from typing import Any, Optional
from datetime import datetime, date


def _serialize_value(val: Any) -> Any:
    """Convert non-JSON-serializable values."""
    if isinstance(val, (datetime, date)):
        return val.isoformat()
    return val


def _serialize_data(data: Any) -> Any:
    """Recursively serialize data for JSON compatibility."""
    if data is None:
        return None
    if isinstance(data, dict):
        return {k: _serialize_data(v) for k, v in data.items()}
    if isinstance(data, list):
        return [_serialize_data(item) for item in data]
    return _serialize_value(data)


def api_success(
    message: str = "Success",
    data: Any = None,
    status_code: int = status.HTTP_200_OK
) -> JSONResponse:
    """
    Return a successful API response.
    
    Args:
        message: Human-readable success message
        data: Response data (dict, list, or any serializable object)
        status_code: HTTP status code (default: 200)
    
    Returns:
        JSONResponse with standard structure
    
    Example:
        return api_success("User created", {"id": 1}, status_code=201)
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": True,
            "message": message,
            "data": _serialize_data(data),
            "error": False
        }
    )


def api_error(
    message: str = "An error occurred",
    data: Any = None,
    status_code: int = status.HTTP_400_BAD_REQUEST
) -> JSONResponse:
    """
    Return an error API response.
    
    Args:
        message: Human-readable error message
        data: Additional error details (optional)
        status_code: HTTP status code (default: 400)
    
    Returns:
        JSONResponse with standard structure
    
    Example:
        return api_error("Invalid input", status_code=422)
        return api_error("Not found", status_code=404)
    """
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "data": _serialize_data(data),
            "error": True
        }
    )
