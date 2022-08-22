import logging

from fastapi import Request, FastAPI, APIRouter

from src.app import execute

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

@app.post("/vendors_emergency_projects")
async def vendors_emergency_projects(request: Request):
    body = await request.json()
    return execute(body)
    
app.include_router(router, prefix="/vendors_emergency_projects")

logger.info("Starting up")
