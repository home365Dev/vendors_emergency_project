import logging

from fastapi import Request, FastAPI, APIRouter

from src.vendors_emergency_projects.app import execute

import json

logger = logging.getLogger(__name__)
logging.basicConfig()


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
    print("00000")
    body = await request.json()
    print("11111111111111111111111")
    result = {
        'statusCode': 200,
        'body': json.dumps({'result': execute(body)})
    }
    return result
    
app.include_router(router, prefix="/vendors_emergency_projects")

logger.info("Starting up")
