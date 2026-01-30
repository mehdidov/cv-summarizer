from fastapi import FastAPI
from app.core.route import router as core_router
from app.routers.cvs import router as cvs_router
from app.routers.ai import router as ai_router


app = FastAPI(title="cv-summarize")

app.include_router(core_router)
app.include_router(cvs_router)
app.include_router(ai_router)

