import logging

import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.routers.glossary_router import router as glossary_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Glossary API",
    version="1.0.0",
    description="REST API для управления терминами",
    contact={"name": "Ivan Monichev", "email": "ivan@monichev.ru", "url": "https://github.com/IvanMonichev"}
)

app.include_router(glossary_router, prefix="/api", tags=["Glossary"])

logger = logging.getLogger("uvicorn")


@app.on_event("startup")
def log_docs_urls():
    host = "127.0.0.1"
    port = 8000
    logger.info(f"Swagger UI: http://{host}:{port}/docs")
    logger.info(f"ReDoc:      http://{host}:{port}/redoc")
    logger.info(f"OpenAPI:    http://{host}:{port}/openapi.json")

