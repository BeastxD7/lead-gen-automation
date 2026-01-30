# Anvesh Automation Server

The core backend automation engine for Anvesh, built with FastAPI and Playwright.

## 🛠️ Tech Stack

*   **Language:** Python 3.12+
*   **Framework:** FastAPI
*   **Database:** PostgreSQL (with `psycopg` binary)
*   **Automation:** Playwright (Chromium)
*   **Package Manager:** [uv](https://github.com/astral-sh/uv)

## 🚀 Setup & Running

### Requirements
- Python 3.12+
- PostgreSQL 15+
- [uv](https://github.com/astral-sh/uv)

### Installation

1.  **Install Dependencies**
    ```bash
    uv sync
    ```

2.  **Environment Setup**
    Copy `.env.example` to `.env.local` and configure your database credentials.
    ```bash
    cp .env.example .env.local
    ```
    
    Required variables:
    ```env
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=password
    DB_NAME=lead_scraper
    ADMIN_SECRET=your-secure-secret
    ```

3.  **Start Database (Docker)**
    Run the database service in the background:
    ```bash
    docker compose up -d db
    ```

4.  **Run the Server**
    ```bash
    uv run uvicorn app.main:app --reload
    ```
    API will be available at [http://localhost:8000](http://localhost:8000).

## 🧪 Testing

Run the comprehensive test suite:
```bash
uv run pytest
```
See [docs/testing.md](docs/testing.md) for details.

## 📚 API Documentation

Detailed API documentation is available in the `docs/` directory:
- [API Overview](docs/api/overview.md)
- [Keys API](docs/api/keys.md)
- [Automation API](docs/api/automation.md)
