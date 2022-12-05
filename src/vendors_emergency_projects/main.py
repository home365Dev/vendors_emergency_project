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


if __name__ == '__main__':
    body = { "text": "**** all right , I m probably gon na regret order point , soon possible master bathroom , uh sort valve continually run water toilet bowl . I try I include go Home Depot try replacement um sort flush mechanism like I use . I figure constant run . so end water drain tank fill night long . its drive crazy . not urgent , certainly go , drain trigger refill . um not good house sort chronically run toilet . tub bathroom toilet bathtub machine", 'project_id': 'c5c6ba50-245f-4be1-aab8-5c68dac1bb64'}
    result_to_dict, project_id_str, input_str = execute(body)
    result = {
        'statusCode': 200,
        'body': result_to_dict
    }
    thread = threading.Thread(target=execute_to_db, kwargs={
        'res_to_dict': result_to_dict, 'id': project_id_str, 'text_of_case': input_str})
    thread.start()
    print("done")