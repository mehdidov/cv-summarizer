from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(
    prefix="/cvs",
    tags=["cvs"]
)

@router.post("/upload")
async def cv_upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code = 415,
            detail = "Unsupported Media Type"
        )
    return {
        "filename": file.filename
    
    }