from functools import lru_cache

from databases import Database
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import MetaData

from dentalcrm.settings import Settings


@lru_cache
def get_settings():
    return Settings()


@lru_cache
def get_database():
    settings = get_settings()
    return Database(url=settings.database_url)


@lru_cache
def get_metadata():
    return MetaData()


@AuthJWT.load_config
def get_config():
    return Settings()
