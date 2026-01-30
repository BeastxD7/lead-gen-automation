"""
API Key tier configuration.
"""
from typing import Dict

# Tier Configuration (easily modifiable)
# monthly_limit: -1 means unlimited
TIERS: Dict[str, Dict] = {
    "free": {
        "monthly_limit": 100,
        "rate_limit_per_minute": 10,
        "description": "Free tier - 100 leads/month"
    },
    "pro": {
        "monthly_limit": 5000,
        "rate_limit_per_minute": 60,
        "description": "Pro tier - 5000 leads/month"
    },
    "enterprise": {
        "monthly_limit": -1,  # Unlimited
        "rate_limit_per_minute": 300,
        "description": "Enterprise tier - Unlimited"
    }
}


def get_tier_limit(tier: str) -> int:
    """Get monthly limit for a tier. Returns -1 for unlimited."""
    return TIERS.get(tier, TIERS["free"])["monthly_limit"]


def get_tier_rate_limit(tier: str) -> int:
    """Get rate limit per minute for a tier."""
    return TIERS.get(tier, TIERS["free"])["rate_limit_per_minute"]
