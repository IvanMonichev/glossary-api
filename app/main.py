from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from uvicorn.server import logger

from app.core.config import settings
from app.core.database import Base, engine
from app.routers.glossary_router import router as glossary_router

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    host = settings.app_host
    port = settings.app_port
    logger.info(f"Environment: {settings.app_env.upper()}")
    logger.info(f"Swagger UI: http://{host}:{port}/docs")
    logger.info(f"ReDoc:      http://{host}:{port}/redoc")
    logger.info(f"OpenAPI:    http://{host}:{port}/openapi.json")
    yield
    logger.info("Application shutdown...")


app = FastAPI(
    title="Glossary API",
    version="1.0.0",
    description="REST API для управления терминами",
    contact={
        "name": "Ivan Monichev",
        "email": "ivan@monichev.ru",
        "url": "https://github.com/IvanMonichev"
    },
    lifespan=lifespan
)

app.include_router(glossary_router, prefix="/api", tags=["Glossary"])

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.is_dev,
        log_level="debug" if settings.is_dev else "info",
    )
