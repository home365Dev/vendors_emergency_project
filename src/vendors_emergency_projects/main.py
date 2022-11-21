import logging

from fastapi import Request, FastAPI, APIRouter
from src.vendors_emergency_projects.db_handler import execute_to_db
from src.vendors_emergency_projects.app import execute
import src.vendors_emergency_projects.logger as logger
import threading
router = APIRouter()

app = FastAPI(
    title="Home365",
    version="0.0.1",
)

@router.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@router.post("/vendors_emergency_projects")
async def vendors_emergency_projects(request: Request):
    body = await request.json()
    result_to_dict, project_id_str, input_str = execute(body)
    result = {
        'statusCode': 200,
        'body': result_to_dict
    }
    thread = threading.Thread(target=execute_to_db, kwargs={
        'res_to_dict': result_to_dict, 'id': project_id_str, 'text_of_case': input_str})
    thread.start()
    return result
    
app.include_router(router, prefix="/vendors_emergency_projects")

logger.info("Starting up")
