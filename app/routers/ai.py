from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pdf_to_image import pdf_to_images
from app.services.openrouter_client import send_image_to_ai

router = APIRouter(prefix="/ai", tags=["ai"])

PDF_DIR = Path("uploads/pdf")

@router.post("/analyze/{cv_id}")
def analyze_cv(cv_id: str):
    pdf_path = PDF_DIR / f"{cv_id}.pdf"

    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="PDF not found")

    images = pdf_to_images(pdf_path, cv_id)

    responses = []
    for img in images:
        ai_response = send_image_to_ai(
            img,
            "content of CV image"
        )
        responses.append(ai_response)

    return {
        "cv_id": cv_id,
        "analysis": responses
    }
