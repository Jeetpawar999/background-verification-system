from fastapi import APIRouter, UploadFile, File, Form
import os
from app.orchestration.reexecutor import reexecute

from app.audit.audit_logger import get_audit_history
from app.orchestration.orchestrator import execute_verification

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/verify")
async def verify(
    full_name: str = Form(...),
    dob: str = Form(...),
    address: str = Form(...),
    government_id: str = Form(...),
    aadhaar_image: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        aadhaar_image.filename
    )

    with open(file_path, "wb") as f:
        f.write(await aadhaar_image.read())

    candidate_data = {
        "full_name": full_name,
        "dob": dob,
        "address": address,
        "government_id": government_id,
        "aadhaar_image": file_path
    }

    result = await execute_verification(
        candidate_data
    )

    return result


@router.get("/audit")
def audit():

    return get_audit_history()
@router.post("/feedback")
async def feedback(
    feedback: dict
):

    return await reexecute(
        feedback["feedback"]
    )