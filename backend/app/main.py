from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from app.core.constants import APP_DESCRIPTION
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    description=APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(
    router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Welcome to Saarthi AI 🚀",
        "version": settings.APP_VERSION,
    }