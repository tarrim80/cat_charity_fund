from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "QRКот"
    app_description: str = "Донаты на котов."
    database_url: str = "sqlite+aiosqlite:///./fastapi.db"  # для теста
    secret: str = "SECRET"
    min_password_lenght: int = 3
    lifetime_jwt: int = 3600

    class Config:
        env_file = ".env"


settings = Settings()
