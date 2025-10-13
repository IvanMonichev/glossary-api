from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Glossary API'
    app_port: int = 8000
    app_version: str
    app_description: str = 'API для управления терминами и определениями'
    db_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
