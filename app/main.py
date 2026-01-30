from fastapi import FastAPI
from app.routers import automation, keys
from app.db import init_db

app = FastAPI(
    title="Anvesh API",
    description="Lead generation engine that hunts for high-value businesses with zero online presence.",
    version="1.0.0"
)

# Initialize Database
init_db()

# Include Routers
app.include_router(automation.router)
app.include_router(keys.router)