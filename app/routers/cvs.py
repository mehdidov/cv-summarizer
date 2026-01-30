from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/cvs",
    tags=["cvs"]
)

router.post("/upload")
async def cv_upload(file: UploadFile = File(...)):
    return {
        "filename": file.filename
    
    }