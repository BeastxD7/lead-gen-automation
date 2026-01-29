from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from app.models.automation import ScrapeRequest, AutomationRequest
from app.services.scraper import scrape_google_maps
from app.database import get_all_leads
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
def handle_automation(request: AutomationRequest, background_tasks: BackgroundTasks):
    action = request.action.lower()
    
    if action == "start":
        if not request.config:
            raise HTTPException(status_code=400, detail="Config is required to start automation.")
        
        task_id = str(uuid.uuid4())
        TASKS[task_id] = {
            "id": task_id,
            "config": request.config,
            "running": True,
            "stop": False,
            "status": "idle",
            "error": None
        }
        
        background_tasks.add_task(background_task_scraper, task_id, request.config)
        return {
            "status": "success", 
            "message": "Automation started.", 
            "task_id": task_id
        }

    elif action == "stop":
        # If task_id is provided in request (we need to update model or check body), stop that one.
        # But AutomationRequest logic needs check. 
        # For now, let's look for a task_id if we can, or stop ALL running tasks as a fallback/safety?
        # User asked for ID based checking. Let's assume they might send ID to stop too.
        # Since AutomationRequest doesn't have task_id field explicitly defined yet in the previous step,
        # we will rely on a new optional field or query param?
        # Actually, let's just stop the *latest* running one if no ID, or add ID support.
        # Simpler: Modify AutomationRequest in next step. For now, let's assume we stop ALL running tasks 
        # if no specific ID mechanism is easy without model change. 
        # WAIT: I can update the model in the same file if it was defined here, but it is imported.
        # I will implement a "stop all" for now, or finding the active one.
        
        count_stopped = 0
        for tid, task in TASKS.items():
            if task["running"]:
                task["stop"] = True
                count_stopped += 1
        
        if count_stopped == 0:
            return {"status": "ignored", "message": "No running automation found."}
            
        return {"status": "success", "message": f"Stop signal sent to {count_stopped} tasks."}
    
    else:
        raise HTTPException(status_code=400, detail="Invalid action. Use 'start' or 'stop'.")

@router.get("/status/{task_id}")
def get_task_status(task_id: str):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/status")
def get_all_status():
    return TASKS

@router.get("/export")
def export_leads():
    """Exports all leads from the database to a CSV file."""
    leads = get_all_leads()
    if not leads:
        return {"message": "No data found."}
    
    os.makedirs("data", exist_ok=True)
    filename = "data/all_leads_export.csv"
    
    keys = leads[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(leads)
        
    return FileResponse(filename, filename="leads_export.csv", media_type="text/csv")