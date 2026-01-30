# API Overview

## Authentication

All API endpoints require authentication via API keys passed in the `X-API-Key` header.

Admin endpoints additionally require `X-Admin-Secret` header.

## Response Format

All responses follow a standardized structure:

```json
{
  "success": true,
  "message": "Human readable message",
  "data": { ... },
  "error": false
}
```

## Tier Limits

| Tier | Monthly Leads | Rate Limit |
|------|---------------|------------|
| Free | 100 | 10/min |
| Pro | 5,000 | 60/min |
| Enterprise | Unlimited | 300/min |

## API Sections

- [Keys API](keys.md) - API key management (admin & user)
- [Automation API](automation.md) - Scraping and lead generation
