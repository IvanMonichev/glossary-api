from pathlib import Path

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str = 'Glossary API'
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_version: str
    app_description: str = 'API для управления терминами и определениями'
    db_url: str
    app_env: str = "dev"

    @property
    def is_dev(self) -> bool:
        return self.app_env.lower() == "dev"

    @property
    def is_prod(self) -> bool:
        return self.app_env.lower() == "prod"

    class Config:
        env_file = Path(__file__).resolve().parent.parent.parent / ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
