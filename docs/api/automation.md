# Automation API

Lead generation and scraping endpoints.

> All endpoints require `X-API-Key` header

## Start/Stop Automation
`POST /automation`

### Start Scraping

```bash
curl -X POST http://localhost:8000/automation \
  -H "X-API-Key: anv_your_key" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "start",
    "config": {
      "industry": "dentist",
      "locations": ["New York, NY", "Los Angeles, CA"],
      "limit_per_location": 50
    }
  }'
```

**Response (201):**
```json
{
  "success": true,
  "message": "Automation started",
  "data": {
    "task_id": "abc-123-def-456"
  }
}
```

### Stop All Running Tasks

```bash
curl -X POST http://localhost:8000/automation \
  -H "X-API-Key: anv_your_key" \
  -d '{"action": "stop"}'
```

---

## Get All Task Statuses
`GET /status`

```bash
curl http://localhost:8000/status \
  -H "X-API-Key: anv_your_key"
```

---

## Get Specific Task Status
`GET /status/{task_id}`

```bash
curl http://localhost:8000/status/abc-123-def-456 \
  -H "X-API-Key: anv_your_key"
```

---

## Export Leads
`GET /export`

Downloads all scraped leads as a CSV file.

```bash
curl http://localhost:8000/export \
  -H "X-API-Key: anv_your_key" \
  -o leads.csv
```
