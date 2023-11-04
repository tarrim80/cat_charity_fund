from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "QRКот"
    app_description: str = "Донаты на котов."
    database_url: str
    db_echo: bool = True
    secret: str = "SECRET"

    class Config:
        env_file = ".env"


settings = Settings()
