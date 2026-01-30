# Testing Guide

Anvesh uses **pytest** for testing with a mix of unit and integration tests.

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run only unit tests
uv run pytest tests/unit/

# Run only integration tests
uv run pytest tests/integration/
```

## Test Structure

```
tests/
├── conftest.py           # Shared fixtures
├── unit/                 # Unit tests (isolated functions)
│   ├── test_api_keys.py  # API key generation & validation
│   └── test_db.py        # Database operations
└── integration/          # Integration tests (HTTP requests)
    ├── test_middleware.py    # Auth middleware
    ├── test_keys.py          # Key management routes
    └── test_automation.py    # Automation routes
```

## Test Categories

### Unit Tests
Test individual functions in isolation:
- API key generation and hashing
- Key validation logic
- Usage logging functions
- Database CRUD operations

### Integration Tests
Test full request/response cycles via FastAPI TestClient:
- Authentication middleware (valid/invalid keys)
- Admin endpoints (create, list, delete keys)
- User endpoints (view info, usage stats)
- Automation endpoints (start, stop, status)

## Fixtures

Common fixtures are defined in `conftest.py`:

| Fixture | Description |
|---------|-------------|
| `client` | FastAPI TestClient instance |
| `admin_headers` | Headers with valid admin secret |
| `test_api_key` | Creates a test API key (cleaned up after) |
| `user_headers` | Headers with valid user API key |

## Environment Variables

Tests require:
```env
ADMIN_SECRET=test-admin-secret
DB_NAME=lead_scraper  # or lead_scraper_test
```

## CI/CD

Tests run automatically on every PR via GitHub Actions (`.github/workflows/test.yml`).

The workflow:
1. Spins up PostgreSQL service container
2. Installs dependencies with `uv`
3. Installs Playwright browsers
4. Runs `pytest`
