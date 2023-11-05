from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "QRКот"
    app_description: str = "Донаты на котов."
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"  # для теста
    secret: str = "SECRET"

    class Config:
        env_file = ".env"


settings = Settings()
