from pydantic import BaseModel
from typing import List, Optional

class ScrapeRequest(BaseModel):
    industry: str
    locations: List[str]
    limit_per_location: Optional[int] = -1

class AutomationRequest(BaseModel):
    action: str  # "start" | "stop"
    config: Optional[ScrapeRequest] = None
