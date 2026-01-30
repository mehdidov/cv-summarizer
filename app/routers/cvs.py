from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(
    prefix="/cvs",
    tags=["cvs"]
)

MAX_FILE_SIZE = 5 * 1024 * 1024

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
    
    return {
        "filename": file.filename
    
    }