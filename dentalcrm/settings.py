from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    database_url: str
    authjwt_secret_key: str

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"
