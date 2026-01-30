from fastapi import APIRouter, BackgroundTasks, Depends
from fastapi.responses import FileResponse
from app.models.automation import ScrapeRequest, AutomationRequest
from app.models.api_key import APIKeyData
from app.services.scraper import scrape_google_maps
from app.db import get_all_leads, log_usage
from app.middleware.auth import get_api_key
from app.helpers import api_success, api_error
import csv
import os
import uuid

router = APIRouter(tags=["Automation"])

# In-Memory Storage for Tasks
TASKS = {}

def background_task_scraper(task_id: str, request: ScrapeRequest):
    """
    Runs the scraper in the background for a specific task ID.
    """
    print(f"▶️ Automation Started: {request.industry} (ID: {task_id})")
    TASKS[task_id]["status"] = "running"
    
    try:
        total_locations = len(request.locations)
        for i, loc in enumerate(request.locations):
            if TASKS[task_id]["stop"]:
                TASKS[task_id]["status"] = "stopped"
                print(f"🛑 Automation {task_id} stopped by user.")
                break
                
            print(f"📍 [{i+1}/{total_locations}] Processing location: {loc} (ID: {task_id})")
            
            should_stop = lambda: TASKS[task_id]["stop"]
            
            scrape_google_maps(
                industry=request.industry, 
                location=loc, 
                total=request.limit_per_location,
                stop_signal=should_stop
            )
            
            if not TASKS[task_id]["stop"]:
                print(f"✅ Finished location: {loc}. Checking next...")
        
        # If we finished the loop and weren't stopped
        if not TASKS[task_id]["stop"]:
             TASKS[task_id]["status"] = "completed"

    except Exception as e:
        TASKS[task_id]["status"] = "error"
        TASKS[task_id]["error"] = str(e)
        print(f"❌ Automation {task_id} Error: {e}")
    finally:
        TASKS[task_id]["running"] = False
        print(f"🏁 Automation {task_id} Finished. Status: {TASKS[task_id]['status']}")

@router.post("/automation")
def handle_automation(
    request: AutomationRequest,
    background_tasks: BackgroundTasks,
    api_key: APIKeyData = Depends(get_api_key)
):
    action = request.action.lower()
    
    # Log the API usage
    log_usage(api_key.id, "/automation", 0)
    
    if action == "start":
        if not request.config:
            return api_error("Config is required to start automation", status_code=400)
        
        task_id = str(uuid.uuid4())
        TASKS[task_id] = {
            "id": task_id,
            "config": request.config.model_dump(),
            "running": True,
            "stop": False,
            "status": "idle",
            "error": None
        }
        
        background_tasks.add_task(background_task_scraper, task_id, request.config)
        return api_success("Automation started", {"task_id": task_id}, status_code=201)

    elif action == "stop":
        count_stopped = 0
        for tid, task in TASKS.items():
            if task["running"]:
                task["stop"] = True
                count_stopped += 1
        
        if count_stopped == 0:
            return api_success("No running automation found", {"tasks_stopped": 0})
            
        return api_success(f"Stop signal sent to {count_stopped} tasks", {"tasks_stopped": count_stopped})
    
    else:
        return api_error("Invalid action. Use 'start' or 'stop'", status_code=400)

@router.get("/status/{task_id}")
def get_task_status(task_id: str, api_key: APIKeyData = Depends(get_api_key)):
    task = TASKS.get(task_id)
    if not task:
        return api_error("Task not found", status_code=404)
    return api_success("Task status retrieved", task)

@router.get("/status")
def get_all_status(api_key: APIKeyData = Depends(get_api_key)):
    return api_success("All tasks retrieved", TASKS)

@router.get("/export")
def export_leads(api_key: APIKeyData = Depends(get_api_key)):
    """Exports all leads from the database to a CSV file."""
    log_usage(api_key.id, "/export", 0)
    
    leads = get_all_leads()
    if not leads:
        return api_success("No data found", {"count": 0})
    
    os.makedirs("data", exist_ok=True)
    filename = "data/all_leads_export.csv"
    
    keys = leads[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(leads)
        
    return FileResponse(filename, filename="leads_export.csv", media_type="text/csv")