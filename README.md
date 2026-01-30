# 🦅 Anvesh (अन्वेष)

> **An automated intelligence engine that hunts for high-value businesses with zero online presence.**

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128+-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)

**Anvesh** (Sanskrit for *Investigation/Research*) is a modern, high-performance lead generation engine made with ❤️ in **Bharat**. It acts as a virtual research assistant that dives into the "Blue Ocean" of profitable businesses (Roofers, Dentists, Manufacturers) that have high revenue but **no website**.

## ✨ Key Features

*   **💰 Zero API Costs:** Uses Playwright to scrape data directly, bypassing expensive API subscriptions.
*   **🌍 Anti-Geoblocking:** Automatically configures browser context to block local IP bias.
*   **🧠 Smart De-duplication:** Detects and ignores duplicate listings using PostgreSQL constraints.
*   **🔐 API Key Authentication:** Enterprise-grade API key management with tiered access.
*   **📈 Usage Tracking:** Built-in usage logging and quota management per API key.
*   **🐳 Docker Ready:** Full stack setup with a single command.

## 🛠️ Tech Stack

*   **Language:** Python 3.12+
*   **Framework:** FastAPI
*   **Database:** PostgreSQL
*   **Automation:** Playwright (Chromium)
*   **Package Manager:** [uv](https://github.com/astral-sh/uv)

## 🚀 Quick Start

### Docker (Recommended)
```bash
docker compose up --build
```
API available at [http://localhost:8000](http://localhost:8000)

### Local Development
```bash
uv sync
cp .env.example .env.local
uv run uvicorn app.main:app --reload
```

### Environment Variables
```env
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=lead_scraper
ADMIN_SECRET=your-secure-admin-secret
```

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [API Overview](docs/api/overview.md) | Auth, response format, tiers |
| [Keys API](docs/api/keys.md) | API key management |
| [Automation API](docs/api/automation.md) | Scraping endpoints |
| [Testing Guide](docs/testing.md) | Test structure and CI/CD |

## 🔐 Quick API Example

```bash
# Create API key (admin)
curl -X POST http://localhost:8000/admin/keys \
  -H "X-Admin-Secret: your-secret" \
  -d '{"name": "My App", "tier": "free"}'

# Use the key
curl http://localhost:8000/me/usage \
  -H "X-API-Key: anv_your_key"
```

## 🧪 Testing

```bash
uv run pytest
```

See [Testing Guide](docs/TESTING.md) for more details.

## 🇮🇳 Made in Bharat

Anvesh is built to empower freelancers and small agencies worldwide by providing professional-grade tools at zero cost.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.
