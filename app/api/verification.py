from fastapi import APIRouter, UploadFile, File, Form
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/verification/start")
async def start_verification(
    full_name: str = Form(...),
    dob: str = Form(...),
    address: str = Form(...),
    government_id: str = Form(...),
    aadhaar_image: UploadFile = File(...),
    pan_image: UploadFile = File(None)
):

    aadhaar_path = os.path.join(
        UPLOAD_DIR,
        aadhaar_image.filename
    )

    with open(aadhaar_path, "wb") as f:
        f.write(await aadhaar_image.read())

    return {
        "full_name": full_name,
        "dob": dob,
        "address": address,
        "government_id": government_id,
        "aadhaar_image": aadhaar_image.filename
    }