from fastapi import FastAPI

from app.api.router import router
from app.core.config import settings
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(
    router,
    prefix=settings.API_V1_PREFIX,
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Saarthi AI 🚀"
    }