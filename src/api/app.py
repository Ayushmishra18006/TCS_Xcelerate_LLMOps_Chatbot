from fastapi import FastAPI
from src.api.health_check import router as health_router
from src.utils.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(health_router)

@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} Running"
    }