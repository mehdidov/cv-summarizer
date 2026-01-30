from fastapi import FastAPI
from app.core.route import router as core_router

app = FastAPI(title="cv-summarize")

app.include_router(core_router)
