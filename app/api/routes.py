from fastapi import APIRouter
from app.models.schemas import Candidate
from app.orchestration.orchestrator import execute_verification

router = APIRouter()

@router.post("/verify")
async def verify(candidate: Candidate):

    result = await execute_verification(
        candidate.dict()
    )

    return result