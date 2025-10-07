from fastapi import FastAPI
from app.routers.glossary_router import router as glossary_router

app = FastAPI(
    title="Glossary API",
    version="1.0.0",
    description="REST API для управления терминами",
    contact={"name": "Ivan Monichev", "email": "ivan@monichev.ru", "url": "https://github.com/IvanMonichev"}
)

app.include_router(glossary_router, prefix="/api", tags=["Glossary"])
