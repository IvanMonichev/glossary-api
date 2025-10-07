from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "REST API Glossary"
    DATABASE_URL: str = "sqlite:"

    class Config(object):
        env_file = ".env"


settings = Settings()
