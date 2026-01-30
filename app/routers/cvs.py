import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

router = APIRouter(
    prefix="/cvs",
    tags=["cvs"]
)

MAX_FILE_SIZE = 5 * 1024 * 1024
cv_upload_dir = Path("uploads")
if not cv_upload_dir.exists():
    cv_upload_dir.mkdir(parents=True)

@router.post("/upload")
async def cv_upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code = 415,
            detail = "Unsupported Media Type"
        )
    
    file_content = await file.read()
    if len(file_content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code = 413,
            detail = "Payload Too Large"
        )
    
    cv_id = str(uuid.uuid4())

    file_path = cv_upload_dir / f"{cv_id}.pdf"

    with open(file_path, "wb") as f:
        f.write(file_content) 
    
    return {
        "id": cv_id,
        "filename": file.filename
    
    }